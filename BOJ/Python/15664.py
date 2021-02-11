def c(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in c(arr[i+1:],r-1):
                yield [arr[i]]+next        
n,m=map(int,input().split())
n=list(map(int,input().split()))
n.sort()
t=[]
for i in c(n,m):
    t.append(tuple(i))

for j in sorted(list(set(t))):
    print(*j)
