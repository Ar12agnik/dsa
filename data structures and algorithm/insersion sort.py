#each element asks the previous element ami ki tormar #theke choto?
#first part sorted 19 sorted 
x=[19,18,17,16,15,14,13,12,11,4]
for i in range(0,len(x)):
    for j in range(i,-1,-1):
        if j-1>-1:
            if x[j-1]>x[j]:
                x[j],x[j-1]=x[j-1],x[j]
print(x)
