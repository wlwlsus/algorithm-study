from itertools import product as p
n,m=map(int,input().split())
for i in p(range(1,n+1),repeat=m):
    print(*i)