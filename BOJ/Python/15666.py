def cwr(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in cwr(arr[i:], r-1):
                yield [arr[i]] + next
    
n,m=map(int,input().split())
n=list(map(int,input().split()))
n.sort()
t=[]
for i in cwr(n,m):
    t.append(tuple(i))

for j in sorted(list(set(t))):
    print(*j)