import abc


class Encoded:
    __metaclass__ = abc.ABCMeta

    def encode(self, string: str) -> bytes:
        """Encode the class into a Binary"""
        return string.encode('utf-8')

    def decode(self, bytes: bytes) -> str:
        """Decode the class into a String"""
        return bytes.decode('utf-8')