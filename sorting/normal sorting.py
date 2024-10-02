'''
find smallest element and put it at the end of the sorted array
for first element put it at the front
'''
x=[12,9,30,45,85,10,3,0]
for i in range(0,len(x)):
    for j in range((i+1),len(x)):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
        print(x)
        
print(x)