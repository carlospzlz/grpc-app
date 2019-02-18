Client/Server Application
=========================
This is a simple client/server app that uses the gRPC protocol to exchange data.
Data can be one **number**, one **string** or one **file**.

Dependencies
------------
This project was developed and tested with the versions listed below.

| Name          | Version                |
| ------------- |:----------------------:|
| C++ compiler  | GCC 8.2.1, Clang 7.0.0 |
| Python        | 3.7.0                  |
| gRPC          | 1.18.0                 |
| Protobuf      | 3.6.1                  |
| Nosetests     | 1.3.7                  |

*Nosetests is just needed to run the tests.*

Clone and Build
-----
To clone and build this project you need to run the following lines:
```
git clone git@github.com:carlospzlz/grpc_app.git
cd grpc_app
make
```

Run the Server
--------------
To run the server you need to provide a `hostname` and a `port number`.
```
./server localhost 50051
```

Run the Tests
-------------
Some tests are provided with this project to verify the correct functioning of the system.
```
nosetests -v
```
You should be able to see an output like this:
```
test_getFile_grpc_png (tests.TestGetFile) ... ok
test_getFile_helloworld_tar (tests.TestGetFile) ... ok
test_getFile_helloworld_txt (tests.TestGetFile) ... ok
test_getFile_raises_FileExistsError (tests.TestGetFile) ... ok
test_getNumber_one (tests.TestGetNumber) ... ok
test_getNumber_three (tests.TestGetNumber) ... ok
test_getNumber_two (tests.TestGetNumber) ... ok
test_getString_index_0 (tests.TestGetString) ... ok
test_getString_index_1 (tests.TestGetString) ... ok
test_getString_index_3 (tests.TestGetString) ... ok
test_getString_raises_TypeError (tests.TestGetString) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.219s

OK
```
*The tests assume that the server is running in localhost:50051*

Run the Client
--------------
The Client is a simple Python script that can be run to perform requests to the server.

#### Requesting one Number
To request a number you need to provide the name of that number.
```
./client --request number one
```
*Only the one, two, three and four are available*

#### Requesting one String
To request a string you need to provide the index in the server's storage vector.
```
./client --request string 0
```
*The storage vector has size 5*

#### Requesting one File
To request a file you need to provide the file path.
```
./client --request file files/helloworld.txt
```
The file will be transmitted and copied to the current directory.
