def cwr(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in cwr(arr[i:],r-1):
                yield [arr[i]]+next

n,m=map(int,input().split())
n=list(map(int,input().split()))
n.sort()
for i in cwr(n,m):
    print(*i)