import unittest

import hashlib

import grpc

import app_pb2_grpc

import client_core


# Using default hostname and port number.
ENDPOINT = 'localhost:50051'


class TestGetNumber(unittest.TestCase):
    """
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

def TestGetFile(unittest.TestCase):
    """
    """
    BASEDIR = 'files'

    @classmethod
    def setUpClass(cls):
        self.__testFiles = ('helloworld.txt', 'helloworld.tar');
        for filename in testFiles:
            assert os.path.isfile(os.path.join(cls.BASEDIR, filename))
            assert not os.path.isfile(filename))

   @classmethod
    def tearDownClass(cls):
        for filename in self.__testFiles:
            if os.path.isfile(filename):
                os.remove(filename)

    def __assertFilesAreEqual(self, filepath1, filepath2):
        hashes = []
        for filname in (filepath1, filepath2):
            with open(filename, 'br') as file_:
                content = file_.read()
                sha1Hash = hashlib.sha1(content)
                hashes.append(sha1Hash.hexdigest())
        self.assertEqual(hashes[0], hashes[1])

    def test_getFile_helloworld_txt(self):
        filename = 'helloworld.txt'
        filepath = os.path.join(self.BASEDIR, filename)
        with grpc.insecure_channel(ENDPOINT) as channel:
            stub = app_pb2_grpc.DataServiceStub(channel)
            result = client_core.getFile(filepath)
        self.assertEqual(result, filename)
        self.__assertFilesAreEqual(result, filepath)



 


