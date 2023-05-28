x=[19,18,17,16,15,14,13,12,11,4]
arr=[[],[],[],[],[],[],[],[],[],[]]
for i in x:
    arr[i%10].append(i)
print(f"original array{x}")
sorted=[]
final_sorted=[]
for i in arr:
    for j in i:
        sorted.append(j)
arr2=[[],[],[],[],[],[],[],[],[],[]]

for i in sorted:
    arr2[i//10].append(i)
for i in arr2:
    for j in i:
        final_sorted.append(j)
print(final_sorted)