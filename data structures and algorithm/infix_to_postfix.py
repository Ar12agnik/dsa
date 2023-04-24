operators={'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
def push(data):
    global top
    top+=1
    stack.append(data)
def pop():
    global top
    if top==-1:
        return 'underflow'
    else:
        top-=1
        return stack.pop()
stack=[]
top=-1
exp=input("enter the desired expression: ")
postfix=''
for i in exp:
    if i in operators.keys():
        while top!=-1:
            if stack[top][1]<operators[i]:
                push((i,operators[i]))
                break
            else:
                x=pop()
                postfix+=x[0]
        if top==-1:
            push((i,operators[i]))
    else:
        postfix+=i
for j in range(len(stack)):
    a=pop()
    postfix+=a[0]


print(f"infix:{exp}\npostfix:{postfix}")
