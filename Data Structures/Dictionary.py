from UserHashData import UserHashData
from GraphHashData import GraphHashData
from HashData import HashData
from User import User
from tqdm import tqdm
from LinkedList import LinkedList

class OptimizedDictionary:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.keys_as_list = []
        self.values_as_list = []
        self.index = 0
        
    def __iter__(self):
        return self
    
    def toDict(self) -> dict:
        d = dict()
        for key in self.keys_as_list:
            d[key]=self.get(key)
            
        return d

    def __next__(self):
        if self.index>=self.size:
            raise StopIteration
        
        key = self.keys[self.index]
        value = self.values[self.index]
        
        self.index += 1
        return key, value
    
    def items(self):
        d = dict()
        for key in self.keys:
            if key is not None:
                d[key]=self.get(key)
        return d.items()

    def get(self, key):
        hash_key = self.myHash(key)
        
        if self.keys[hash_key] == key:
            return self.values[hash_key]
        
        else:
            for i in range(hash_key,hash_key+self.size):
                i %= self.size
                
                if self.keys[i] == key:
                    return self.values[i]
                
            return None

    def put(self, key, value):
        
        hash_key = self.myHash(key)
        
        if self.keys[hash_key] is None:
            self.keys[hash_key] = key
            self.values[hash_key] = value
            
            
        else:
            for i in range(hash_key,hash_key+self.size):
                
                i %= self.size
                
                if self.keys[i] is None or self.keys[i] == key:
                    
                    self.keys[i] = key
                    
                    self.values[i] = value
                    self.keys_as_list.append(key)
                    self.values_as_list.append(value)
                    
                    break

    def myHash(self, key):
        hsh = 0
        carpan = 3
        for char in key:
            hsh+=carpan * (ord(char) *ord(char) - carpan)-pow(2, carpan)
            carpan += 1
        return hsh % self.size
    
    def getTable(self):
        return self.keys

class Dictionary():
    
    def __init__(self,size) -> None:
        self.size = size
        self.hashtable = [None]*self.size

        
        for i in tqdm(range(self.size),desc="Hash Data atanıyor"):
            h = HashData(None,None)
            self.hashtable[i] = h
            
        print("Hashtable Oluşturuldu")
        
        
    def get(self,key:str):
        if(self.hashtable[self.myHash(key)].key == key):
            return self.hashtable[self.myHash(key)].value
        
        else:
            donus = 0
            indis = self.myHash(key)
            
            while(self.hashtable[indis].key != key and self.hashtable[indis].key!=key):
                indis+=1    
                if(indis>=self.size):
                    if(donus>=1):      
                        return None
                    indis = indis%self.size
                    donus+=1
                    
            return self.hashtable[indis].value
            
    def put(self,hashdata:HashData):
        if(self.hashtable[self.myHash(hashdata.key)] is None):
            self.hashtable[self.myHash(hashdata.key)] = hashdata

            return 1
        else:
            donus = 0
            indis = self.myHash(hashdata.key)
            while(self.hashtable[indis].key is not None and self.hashtable[indis].key != hashdata.key):
                indis+=1
                
                if(indis>=self.size):
                    if(donus>=1):
                        print("Table Dolu")
                        return None
                    indis=indis%self.size
                    donus+=1
            self.hashtable[indis].value = hashdata.value
            self.hashtable[indis].key = hashdata.key
     
        
    def getTable(self):
        return self.hashtable
    
    def getKeys(self):
        liste = []
        for i in self.hashtable:
            liste.append(i.key)
        return liste
    
    def getValues(self):
        liste = []
        for i in self.hashtable:
            liste.append(i.value)
        return liste
    
    def myHash(self,key:str):
        carpan = 3
        hsh = 0
        
        for char in key:
            hsh += carpan * (ord(char) * ord(char)-carpan) - pow(2,carpan)
            carpan+1
            
        return hsh % self.size
        
    
if __name__=="__main__":
    d = OptimizedDictionary()
    d.put("username","bruh")
    print(d)