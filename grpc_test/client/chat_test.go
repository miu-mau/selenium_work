package main

import (
	"context"
	"fmt"
	"testing"
	"time"

	pb "groc_test/proto/grpc-chat/chat"

	"google.golang.org/grpc"
)

func getClient(t *testing.T) pb.ChatServiceClient {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		t.Fatalf("did not connect: %v", err)
	}
	return pb.NewChatServiceClient(conn)
}

func TestSendMessage(t *testing.T) {
	client := getClient(t)
	resp, err := client.SendMessage(context.Background(), &pb.MessageRequest{Body: "Hello World"})
	if err != nil {
		t.Fatalf("SendMessage failed: %v", err)
	}
	if resp.Body != "Echo: Hello World" {
		t.Errorf("Unexpected response: %s", resp.Body)
	}
}

func TestSendEmptyMessage(t *testing.T) {
	client := getClient(t)
	resp, err := client.SendMessage(context.Background(), &pb.MessageRequest{Body: ""})
	if err != nil {
		t.Fatalf("SendMessage failed: %v", err)
	}

	expected := "Echo:"
	if resp.Body != expected {
		t.Errorf("Unexpected response: got %s, want %s", resp.Body, expected)
	}
}

func TestMultipleMessages(t *testing.T) {
	client := getClient(t)
	messages := []string{"First", "Second", "Third"}
	for _, msg := range messages {
		resp, err := client.SendMessage(context.Background(), &pb.MessageRequest{Body: msg})
		if err != nil {
			t.Fatalf("SendMessage failed: %v", err)
		}
		expected := "Echo: " + msg
		if resp.Body != expected {
			t.Errorf("Unexpected response: %s", resp.Body)
		}
	}
}

func TestDelayedResponse(t *testing.T) {
	client := getClient(t)
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
	defer cancel()
	resp, err := client.SendMessage(ctx, &pb.MessageRequest{Body: "With Delay"})
	if err != nil {
		t.Fatalf("SendMessage failed: %v", err)
	}
	if resp.Body != "Echo: With Delay" {
		t.Errorf("Unexpected response: %s", resp.Body)
	}
}

func TestConcurrentMessages(t *testing.T) {
	client := getClient(t)
	done := make(chan bool)
	for i := 0; i < 5; i++ {
		go func(i int) {
			msg := fmt.Sprintf("Concurrent %c", 'A'+i)
			resp, err := client.SendMessage(context.Background(), &pb.MessageRequest{Body: msg})
			if err != nil {
				t.Errorf("SendMessage failed: %v", err)
			} else if resp.Body != "Echo: "+msg {
				t.Errorf("Unexpected response: %s", resp.Body)
			}
			done <- true
		}(i)
	}
	for i := 0; i < 5; i++ {
		<-done
	}
}
