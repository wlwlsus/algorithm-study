def combi(arr, r):
    for i in range(len(arr)): 
        if r==1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:],r-1):   
                yield [arr[i]]+next

n,m=map(int,input().split())
n=list(map(int,input().split()))
n.sort()
for i in combi(n,m):
    print(*i)