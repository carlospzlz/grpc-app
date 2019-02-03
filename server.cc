#include <iostream>
#include <memory>

#include <grpcpp/grpcpp.h>

#include "client_server.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using clientserver::DataReply;
using clientserver::DataRequest;
using clientserver::DataService;

class DataServiceImpl final : public DataService::Service
{
    Status GetData(ServerContext* context, const DataRequest* request,
                   DataReply* reply) override
    {
        (void)(context);
        (void)(request);
        reply->set_number(42);
        reply->set_label("Some data");
        return Status::OK;
    }
};

void RunServer()
{
    std::string server_address("0.0.0.0:50051");
    DataServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();
}

int main()
{
    RunServer();
    return 0;
}
