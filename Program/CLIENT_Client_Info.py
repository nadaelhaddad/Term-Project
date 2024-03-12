from collections import UserDict
import json

from UTILS_Serialized import Serialized

class Client_Info(UserDict[str, str], Serialized,):
    def get_nickname(self) -> str:
        """Returns the Nickname of the client."""
        return self.data.get('Nickname', "")

        
    def get_ip(self) -> str:
        return self.data.get('IP', "")

    
    def get_listening_port(self) -> str:
        """Returns the Listening_Port of the client."""
        return self.data.get('Listening_Port', "")

    
    def __init__(self, nickname: str, ip: str, listening_port: str):
        super().__init__()
        # Map the constructor parameters to predefined keys
        self.data = {
            'Nickname': nickname, 
            'IP': ip,    # Public or private IP    
            'Listening_Port': listening_port 
        }
  
    def __setitem__(self, key: str, item: str):
        if key in self.data:
            super().__setitem__(key, item)
        else:
            raise KeyError(f"Key {key} is not defined.")
        
    def serialize(self) -> str:
        """Converts the object to a JSON string."""
        return json.dumps(self.data)

    @staticmethod
    def deserialize(json_str: str):
        """Converts a JSON string back into an instance of PredefinedDict."""
        data = json.loads(json_str)
        # Ensure that the data keys match the predefined keys.
        # This could be more sophisticated based on requirements,
        # like checking for missing keys or extra keys.
        return Client_Info(nickname=data.get('Nickname', ''),
                              ip=data.get('IP', ''),
                              listening_port=data.get('Listening_Port', ''))

