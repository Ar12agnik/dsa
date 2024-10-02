class hashTable:
    def __init__(self):
        self.max=100
        self.array=[None for i in range(self.max)]
    def get_hash(self,key):
        s=0
        for i in key:
            s+=ord(i)
        return s%self.max
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        self.array[h]=value
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.array[h]
ht=hashTable()
ht["hello"]=111
ht["bye"]=333
print(ht["hello"])
print(ht.array)