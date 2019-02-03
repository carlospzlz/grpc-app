export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

all: server client

# Messages
app.pb.o: app.proto
	protoc --cpp_out=. app.proto && \
	g++ -std=c++11 `pkg-config --cflags protobuf grpc`  -c -o app.pb.o app.pb.cc

app_pb2.py: app.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. app.proto

# Services
app.grpc.pb.o: app.pb.o
	protoc --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin`  app.proto && \
	g++ -std=c++11 `pkg-config --cflags protobuf grpc`  -c -o app.grpc.pb.o app.grpc.pb.cc

app_pb2_grpc.py: app.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. route_guide.proto

server: server.cc app.grpc.pb.o
	g++ -std=c++11 `pkg-config --cflags protobuf grpc` -c -o server.o server.cc && \
	g++ app.pb.o app.grpc.pb.o server.o -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc` -o server

client: app_pb2.py app_pb2_grpc.py

clean:
	rm app.grpc.pb.h
	rm app.grpc.pb.cc
	rm app.pb.h
	rm app.pb.cc
	rm *.o
	rm server
	rm app_pb2.py
	rm app_pb2_grpc.py
