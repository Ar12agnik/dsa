class HashTable:
    def __init__(self,max):
        self.Max=max
        self.array=[None for i in range(0,self.Max)]
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.Max
    def add(self,key,value):
        hash=self.get_hash(key)
        print(hash)
        self.array[hash]=value
ht=HashTable(100)
ht.add("hello world","abc")
print(ht.array)