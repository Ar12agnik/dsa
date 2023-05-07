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
    for i in range(front,rear+1):
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
    if (front <=0) and (rear>front):
        print("overflow: please delete atleast one element from front  to insert another one in the front")
    else:
        front-=1
        DEqueue[front]=element

import numpy as np
DEqueue=np.zeros(11,dtype='int16')
front=0
rear=-1
while True:
    n=int(input("1)enqueue at front\n2)enqueue at end\n3)dequeue at front\n4)dequeue at end\n5)print queue\n6)quit\nEnter your choice: "))
    if n==1:
        enqueuefront(int(input("enter any number: ")))
    elif n==2:
        enqueueRear(int(input("enter a number: ")))
    elif n==3:
        dequeuefront()

    elif n==4:
        dequeuerear()
    elif n==5:
        printDEQueue()
    elif n==6:
        break
    else:
        print("invalid input!")