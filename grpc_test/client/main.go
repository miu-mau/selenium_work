package main

import (
	"context"
	"log"
	"time"

	pb "groc_test/proto/grpc-chat/chat"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewChatServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.SendMessage(ctx, &pb.MessageRequest{Body: "Hello from client"})
	if err != nil {
		log.Fatalf("could not send message: %v", err)
	}
	log.Printf("Server response: %s", r.Body)
}
