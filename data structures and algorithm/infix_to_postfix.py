class stack:
    def __init__(self) -> None:
        self.stack=[]
        self.top=-1
    def push(self,element):
        self.stack.append(element)
        self.top+=1
    def pop(self):
        try:
            self.top-=1
            return self.stack.pop()
        except:
            return None
    def access_element_at_top(self):
        return self.stack[-1]
    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
precedence = {
    '(': 1,
    '{': 1,
    '[': 1,
    '^': 2,
    '*': 3,
    '/': 3,
    '+': 4,
    '-': 4
}
stack=stack()
expression=input("enter the expression: ")
output_exp=''
for i in expression:
    if i.lower() in alpha:
        output_exp+=i
    else:
        if stack.isempty():
            stack.push((i,precedence[i]))
        elif i==')':
            while stack.access_element_at_top()[0]!='(':
                output_exp+=stack.pop()
            print(stack.stack)
            output_exp+=stack.pop()
        elif precedence[i]<stack.access_element_at_top()[1]:
            stack.push((i,precedence[i]))
        elif precedence[i]>=stack.access_element_at_top()[1]:
            while precedence[i]>=stack.access_element_at_top()[1]:
                if stack.isempty()!=True:
                    output_exp+=stack.pop()[0]
                else:
                    break
    print(output_exp)
    #DO IT LATER!!!