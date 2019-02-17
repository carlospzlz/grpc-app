import os

import app_pb2


def getNumber(identifier, stub):
    """
    Requests the Number with name `identifier` to the server.
    """
    name = identifier
    response = stub.GetNumber(app_pb2.NumberRequest(name=name))
    return response.number


def getString(identifier, stub):
    """
    Requests the String with index `identifier` to the server.
    """
    if not identifier.isdigit():
        msg = 'ERROR: Identifier expected to be a valid index: {}'
        raise TypeError(msg.format(identifier))
    index = int(identifier)
    response = stub.GetString(app_pb2.StringRequest(index=index))
    return response.string_


def getFile(identifier, stub):
    """
    Requests the File with filepath `identifier` to the server. This method
    will write the received file in the current directory if it does not exist.
    """
    filepath = identifier
    filename = os.path.basename(filepath)
    if os.path.isfile(filename):
        msg = 'ERROR: File already exists: {}'
        raise FileExistsError(msg.format(filepath))
    fileChunks = stub.GetFile(app_pb2.FileRequest(filename=filepath))
    with open(os.path.basename(filename), 'ba') as file_:
        for fileChunk in fileChunks:
            file_.write(fileChunk.content[:fileChunk.size])
    return filename

