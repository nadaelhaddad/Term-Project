import abc


class Serialized:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def serialize(self) -> str:
        """Serialize the class into a String for future encoding"""
        pass

    @abc.abstractmethod
    def deserialize(self, string: str) -> object:
        """Desearilze the class into it's original form"""
        pass
    
    