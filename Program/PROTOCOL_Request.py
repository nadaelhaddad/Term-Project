from enum import Enum
class RequestTypes(Enum):
    NULL = 0
    REGISTER = 1
    DEREGISTER = 2
    RETRIEVE = 3
    RETRIEVEALL = 4
    

class RequestHeader():
    def __init__(self, type = RequestTypes.NULL):
        self.type = type
        

class RequestBody():
    def __init__(self, data = ""):
        self.data = data
        

from UTILS_Encoded import Encoded
from UTILS_Serialized import Serialized
class Request(Serialized, Encoded):
    def __init__(self, header: RequestHeader, body: RequestBody):
        self.header = header
        self.body = body
    
    def serialize(self) -> str:
        return f"{self.header.type.name}:{self.body.data}"
    
    @staticmethod    
    def deserialize(string: str):
        # Splitting the string to extract the type and data
        parts = string.split(':', 1)  # Splits at the first colon only
        if len(parts) != 2:
            raise ValueError("Invalid serialized string format.")
    
        # Converting the string back to a RequestTypes enum
        type_str, data = parts
        header_type = RequestTypes[type_str]  # This assumes type_str is the enum name

        # Creating new instances of MessageHeader and MessageBody
        header = RequestHeader(type=header_type)
        body = RequestBody(data=data)

        # Creating a new Message instance with the deserialized header and body
        return Request(header, body)

    
    def encode_and_serialize(self) -> bytes:
        return self.serialize().encode('utf-8')
    
    @staticmethod
    def decode_and_desearialize(bytes: bytes):
        return Request.deserialize(bytes.decode('utf-8'))