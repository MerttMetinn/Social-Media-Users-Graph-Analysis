from User import User
from HashData import HashData

class UserHashData(HashData):
    def __init__(self,key:str,value:User) -> None:
        super().__init__(key,value)