from heapq import heappush,heappop
def heapsort():
    global list1
    heap=[]
    for ele in list1:
        heappush(heap,ele)
    sort=[]
    while heap:
        sort.append(heappop(heap))
    return sort
