services: client_server.proto
	protoc --grpc_out=. --plugin=protoc-gen-grpc=/usr/local/bin/grpc_cpp_plugin  client_server.proto

messages: client_server.proto
	protoc --cpp_out=. client_server.proto
