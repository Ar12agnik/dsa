import numpy as np
DEqueue=np.zeros(11,dtype='int16')
def isEmpty():
    global rear
    global front
    if rear<front:
        return True
    else:
        return False
def isFull():
    global rear 
    global front 
    if rear==10:
        return True
    else:
        return False
def printDEQueue():
    global rear 
    global front 
    for i in range(front,rear):
        print(DEqueue[i])
def enqueueRear(element):
    global rear 
    if isFull():
        print("Overflow condition:Queue is full please delete some elements first!")
    else:
        rear+=1
        DEqueue[rear]=element
def dequeuefront():
    global front 
    if isEmpty():
        print("underflow:please add something to the queue before you remove any element!!")
    else:
        print(DEqueue[front],"deleted!")
        front+=1
def dequeuerear():
    global rear 
    if isEmpty():
        print("underflow:please add something to the queue before you remove any element!!")
    else:
        print(DEqueue[rear],"deleted!")
        rear-=1
def enqueuefront(element):
    global front 
    if front <=0:
        print("overflow: please delete atleast one element from front  to insert another one in the front")
    else:
        front-=1
        DEqueue[front]=element
#TODO:call the nessesory functions

