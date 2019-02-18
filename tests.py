import hashlib
import os
import unittest

import grpc

import app_pb2_grpc

import client_core


# Using default hostname and port number.
ENDPOINT = 'localhost:50051'


class TestGetNumber(unittest.TestCase):
    """
    Tests for the getNumber RPC.
    """
    def test_getNumber_one(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('one', stub)
        expected = 1
        self.assertEqual(result, expected)

    def test_getNumber_two(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('two', stub)
        expected = 2
        self.assertEqual(result, expected)

    def test_getNumber_three(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getNumber('three', stub)
        expected = 3
        self.assertEqual(result, expected)


class TestGetString(unittest.TestCase):
    """
    Tests for the getString RPC.
    """
    def test_getString_index_0(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getString('0', stub)
        expected = 'foo'
        self.assertEqual(result, expected)

    def test_getString_index_1(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getString('1', stub)
        expected = 'bar'
        self.assertEqual(result, expected)

    def test_getString_index_3(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getString('3', stub)
        expected = 'ham'
        self.assertEqual(result, expected)

    def test_getString_raises_TypeError(self):
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            with self.assertRaises(TypeError):
                result = client_core.getString('a', stub)


class TestGetFile(unittest.TestCase):
    """
    Tests for the getFile RPC.
    """
    BASEDIR = 'files'
    TESTFILES = ('helloworld.txt', 'helloworld.tar', 'grpc.png')

    @classmethod
    def setUpClass(cls):
        for filename in cls.TESTFILES:
            filepath = os.path.join(cls.BASEDIR, filename)
            if not os.path.isfile(filepath):
                msg = 'Test file does not exist: {}'
                raise FileNotFoundError(msg.format(filepath))
            if os.path.isfile(filename):
                msg = 'File already exists in current directory: {}'
                raise FileExistsError(msg.format(filename))

    @classmethod
    def tearDownClass(cls):
        for filename in cls.TESTFILES:
            if os.path.isfile(filename):
                os.remove(filename)

    def __assertFilesAreEqual(self, filepath1, filepath2):
        hashes = []
        for filename in (filepath1, filepath2):
            with open(filename, 'br') as file_:
                content = file_.read()
                sha1Hash = hashlib.sha1(content)
                hashes.append(sha1Hash.hexdigest())
        self.assertEqual(hashes[0], hashes[1])

    def __test_getFile(self, filename):
        filepath = os.path.join(self.BASEDIR, filename)
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getFile(filepath, stub)
        self.assertEqual(result, filename)
        self.__assertFilesAreEqual(result, filepath)

    def test_getFile_helloworld_txt(self):
        self.__test_getFile('helloworld.txt')

    def test_getFile_helloworld_tar(self):
        self.__test_getFile('helloworld.tar')

    def test_getFile_grpc_png(self):
        self.__test_getFile('grpc.png')

    def test_getFile_raises_FileExistsError(self):
        filename = 'helloworld.txt'
        filepath = os.path.join(self.BASEDIR, filename)
        open('helloworld.txt', 'a').close()
        with self.assertRaises(FileExistsError):
            with grpc.insecure_channel(ENDPOINT) as channel:
                stub = app_pb2_grpc.DataServiceStub(channel)
                result = client_core.getFile(filepath, stub)
        os.remove('helloworld.txt')
