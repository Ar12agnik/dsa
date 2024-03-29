#tree using array
import numpy as np
tree=np.zeros(100,dtype="int16")
def insert(element):
    n=0
    while tree[n]!=0:
        if tree[n]>element:
            n=(2*n)+1
        else:
            n=(2*n)+2
    tree[n]=element
def preorder(root):
    if tree[root]==0:
        return
    else:
        print(tree[root])
    preorder((2*root)+1)
    preorder((2*root)+2)
def inorder(root):
    if tree[root]==0:
        return
    inorder((2*root)+1)
    print(tree[root])
    inorder((2*root)+2)
def postorder(root):
    if tree[root]==0:
        return
    postorder((2*root)+1)
    postorder((2*root)+2)
    print(tree[root])
    


insert(50)
insert(35)
insert(15)
insert(10)
insert(18)
insert(40)
insert(38)
insert(45)
insert(9)
insert(67)
insert(99)
print(tree)
print("preorder Traversal:-")
preorder(0)
print("inorder traversal:-")
inorder(root=0)
print("post order Traversal:-")
postorder(root=0)
