from Dictionary import OptimizedDictionary
from tqdm import tqdm


class ArrayList:
    def __init__(self):
        self.size = 100
        self.array = [None]*self.size
        self.itemCount = 0
        
    def contains(self,data):
        for i in self.array:
            if data==i:
                return 1
            
        return 0
    
    def selection_sort(self):
        n = self.itemCount

        for i in tqdm(range(n),desc="Siralaniyor"):
            min_index = i
            for j in range(i+1,n):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            
    def get_top_frequencies(self,top):
        frequency_dict = OptimizedDictionary(800000)

        for i in tqdm(range(self.itemCount),desc="Frekanslar bulunuyor"):
            item = self.array[i]
            if item in frequency_dict.keys_as_list:
                frequency_dict.put(item,frequency_dict.get(item)+1)
            else:
                frequency_dict.put(item,1)
                
        sorted_frequencies = sorted(frequency_dict.items(),key=lambda x: x[1],reverse=True)

        _top = sorted_frequencies[:top]
        
        result = [(word, count) for word, count in _top]

        return result

        
    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < self.itemCount:
            result = self.array[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration
        
    def remove(self, item):
        if item in self.array:
            for i in range(self.array.index(item),self.itemCount - 1):
                self.array[i] = self.array[i + 1]
            self.itemCount-=1
        else:
            return 0


    def add(self,item):
        if(self.itemCount>=self.size):
            
            self.itemCount = 0
            temp = self.array.copy()
            
            self.size *=3
            del self.array
            
            self.array = [None]*self.size
            
            for i in temp:
                self.array[self.itemCount] = i
                self.itemCount+=1
                
            self.array[self.itemCount] = item
            self.itemCount+=1
            
        else:
            
            self.array[self.itemCount] = item
            self.itemCount+=1
            
    def __str__(self):
        mainstr = "["
        for data in self.array:
            if data is None:
                pass
            else:
                mainstr+=str(data)+","

        
        mainstr+="]"
        
        return str(mainstr)
