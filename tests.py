import unittest

import grpc

import app_pb2_grpc

import client_core


# Using default hostname and port number.
ENDPOINT = 'localhost:50051'


class TestGetNumber(unittest.TestCase):
    def test_getNumber_one(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('one', stub)
        expected = 1
        assert result == expected

    def test_getNumber_two(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('two', stub)
        expected = 2
        assert result == expected

    def test_getNumber_three(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('three', stub)
        expected = 3
        assert result == expected


class TestGetString
    def test_getString_index_0(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber(0, stub)
        expected = 'foo'
        assert result == expected

    def test_getString_index_1(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber(1, stub)
        expected = 'bar'
        assert result == expected

    def test_getString_index_3(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('three', stub)
        expected = 'spam'
        assert result == expected


