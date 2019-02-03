export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

all: server

# Messages
client_server.pb.o: client_server.proto
	protoc --cpp_out=. client_server.proto && \
	g++ -std=c++11 `pkg-config --cflags protobuf grpc`  -c -o client_server.pb.o client_server.pb.cc

# Services
client_server.grpc.pb.o: client_server.pb.o
	protoc --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin`  client_server.proto && \
	g++ -std=c++11 `pkg-config --cflags protobuf grpc`  -c -o client_server.grpc.pb.o client_server.grpc.pb.cc


server: server.cc client_server.grpc.pb.o
	g++ -std=c++11 `pkg-config --cflags protobuf grpc` -c -o server.o server.cc && \
	g++ client_server.pb.o client_server.grpc.pb.o server.o -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc` -o server

clean:
	rm client_server.grpc.pb.h
	rm client_server.grpc.pb.cc
	rm client_server.pb.h
	rm client_server.pb.cc
	rm *.o
	rm server
