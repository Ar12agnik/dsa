x=[9,5,7,69,96,1,100,75]
for i in range(0,len(x)):
    for j in range(0,len(x)-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)
