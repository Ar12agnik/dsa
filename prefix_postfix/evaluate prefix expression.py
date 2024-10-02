import numpy as np
top=-1
stack=np.zeros(100)
def push(element,stack):
    global top
    top+=1
    stack[top]=element
def pop(stack):
    global top
    if top>=0:
        top-=1
        return stack[top+1]
    else:
        return False
return_exp=0
x=input("enter the expression in postfix: ")
for i in x:
    if i.isdigit():
        push(int(i),stack=stack)
    else:
        second=pop(stack)
        first=pop(stack)
        temp=''
        temp=temp+str(first)
        temp=temp+i
        temp=temp+str(second)
        push(eval(temp),stack)
print(stack[0])
        
    