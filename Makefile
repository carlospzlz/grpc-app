all: services messages

services: client_server.proto
	protoc --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin`  client_server.proto

messages: client_server.proto
	protoc --cpp_out=. client_server.proto

clean:
	rm client_server.grpc.pb.h
	rm client_server.grpc.pb.cc
	rm client_server.pb.h
	rm client_server.pb.cc
