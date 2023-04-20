#tree using array
import numpy as np
tree=np.zeros(11,dtype="int16")
def insert(element):
    n=0
    while tree[n]!=0:
        if tree[n]>element:
            n=(2*n)+1
        else:
            n=(2*n)+2
    tree[n]=element

insert(50)
insert(35)
insert(15)
insert(10)
insert(18)
insert(40)
insert(38)
insert(45)
insert(90)
insert(67)
insert(99)
print(tree)
