from HashData import HashData
from LinkedList import LinkedList

class GraphHashData(HashData):
    def __init__(self,key:str,value:LinkedList) -> None:
        super().__init__(key,value)