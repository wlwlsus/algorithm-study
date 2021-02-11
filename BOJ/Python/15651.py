# from itertools import product as p
# n,m=map(int,input().split())
# for i in p(range(1,n+1),repeat=m):
#     print(*i)

def f(n,m,k):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            visited[i] = 1
            res[n] = arr[i]
            f(n+1,m,k)
            visited[i] = 0


n, m = map(int, input().split())
arr = range(1,n+1)
visited = [0 for i in range(n)]
res = [0] * m
f(0,n,m)