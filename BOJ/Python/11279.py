import heapq
import sys
n=int(sys.stdin.readline())
heapq_list=[]
for _ in range(n):
    m=int(sys.stdin.readline())
    if m==0:
        if len(heapq_list)==0:
            print(0)
            continue
        else:
            print(heapq.heappop(heapq_list)[1])
            continue
    heapq.heappush(heapq_list, (-m,m))