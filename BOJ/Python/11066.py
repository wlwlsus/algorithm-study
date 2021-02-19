import heapq
n=int(input())
for _ in range(n):
    hq=[]
    size=0
    ans=0

    m=int(input())
    m_list=list(map(int,input().split()))
    for i in m_list:
        heapq.heappush(hq,i)
    
    while len(hq)!=1:
        ans=heapq.heappop(hq) + heapq.heappop(hq)
        size+=ans
        heapq.heappush(hq,ans)

    print(size)