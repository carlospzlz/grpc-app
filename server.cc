#include <iostream>
#include <memory>

#include <grpcpp/grpcpp.h>

#include "app.grpc.pb.h"

using app::DataReply;
using app::DataRequest;
using app::DataService;
using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;

class DataServiceImpl final : public DataService::Service
{
private:
  Status GetData(ServerContext* context, const DataRequest* request,
                 DataReply* reply) override
  {
    (void)(context);
    reply->set_number(m_requestCount);
    reply->set_label(request->name());
    ++m_requestCount;
    return Status::OK;
  }

private:
  std::size_t m_requestCount = 0;
};

void RunServer(const std::string& hostname, const std::string& port)
{
  std::string server_address(hostname + ":" + port);
  DataServiceImpl service;
  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char* args[])
{
  if (argc < 3)
  {
    std::cout << "Usage: ./server <hostname> <port>" << std::endl;
    std::cout << "EXAMPLE" << std::endl;
    std::cout << "    ./server localhost 50051" << std::endl;
    return 1;
  }
  const std::string hostname(args[1]);
  const std::string port(args[2]);
  RunServer(hostname, port);
  return 0;
}
