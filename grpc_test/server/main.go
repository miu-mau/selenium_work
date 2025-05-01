package main

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "groc_test/proto/grpc-chat/chat"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedChatServiceServer
}

func (s *server) SendMessage(ctx context.Context, req *pb.MessageRequest) (*pb.MessageResponse, error) {
	log.Printf("Received message: %s", req.Body)

	// Если сообщение пустое, возвращаем только "Echo:"
	if req.Body == "" {
		return &pb.MessageResponse{Body: "Echo:"}, nil
	}

	return &pb.MessageResponse{Body: "Echo: " + req.Body}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterChatServiceServer(s, &server{})
	fmt.Println("Server is running on port 50051...")
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
