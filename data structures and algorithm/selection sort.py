#selection sort
x=[10,45,16,0,2,-5,6,1,30,99]
for i in range(0,len(x)):
    min_val=x[i]
    min_index=i
    for j in range(i+1,len(x)):
        if min_val>x[j]:
            min_val=x[j]
            min_index=j
    temp=x[i]
    x[i]=x[min_index]
    x[min_index]=temp
print(x)