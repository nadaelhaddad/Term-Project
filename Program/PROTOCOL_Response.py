from enum import Enum

class ResponseTypes(Enum):
    NULL = 000
    SUCCESS = 100
    BAD_REQUEST = 200
    SERVER_ERROR = 300
    

class ResponseHeader():
    def __init__(self, type = ResponseTypes.NULL):
        self.type = type
        

class ResponseBody():
    def __init__(self, data = ""):
        self.data = data
        

from UTILS_Encoded import Encoded
from UTILS_Serialized import Serialized
class Response(Serialized, Encoded):
    def __init__(self, header: ResponseHeader, body: ResponseBody):
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
    
        # Converting the string back to a ResponseTypes enum
        type_str, data = parts
        header_type = ResponseTypes[type_str]  # This assumes type_str is the enum name

        # Creating new instances of ResponseHeader and ResponseBody
        header = ResponseHeader(type=header_type)
        body = ResponseBody(data=data)

        # Creating a new Message instance with the deserialized header and body
        return Response(header, body)

    
    def encode_and_serialize(self) -> bytes:
        return self.serialize().encode('utf-8')
    
    
    @staticmethod
    def decode_and_desearialize(bytes: bytes):
        return Response.deserialize(bytes.decode('utf-8'))