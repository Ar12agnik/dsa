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
    for i in DEqueue:
        print(i)
def enqueueRear(element):
    global rear 
    if isFull():
        print("Overflow condition:Queue is full please delete some elements first!")
    else:
        rear+=1
        DEqueue[rear]=element
#TODO:complete the code
