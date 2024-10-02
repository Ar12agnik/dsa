class HashTable:
    def __init__(self) -> None:
        self.max=100
        self.array=[[] for i in range(self.max)]
    def gethash(self,key):
        s=0
        for i in key:
            s+=ord(i)
        return s%self.max
    def __setitem__(self,key,value):
        hash=self.gethash(key)
        found=False
        for idx, element in enumerate(self.array[hash]):
            if (len(element)==2) and element[0]==key:
                self.array[hash][idx]=(key,value)
                found=True
        if not found:
            self.array[hash].append((key,value))
    def __getitem__(self,key):
        hash=self.gethash(key)
        for i in self.array[key]:
            if i[0]==key:
                return i[1]
    def __delitem__(self,key):
        hash=self.gethash(key)
        for index,ele in enumerate(self.array[hash]):
            if ele[0]==key:
                del self.array[hash][index]
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t.array)
t["march 6"] = 11
print("next")
print(t.array)
del t["march 6"]
print("next")
print(t.array)
