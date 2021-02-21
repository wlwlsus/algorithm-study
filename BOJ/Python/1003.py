def fibo(N):
    cache=[-1 for _ in range(N+1)]
    if N==0:
        pass
        s[0]+=1
        return 0
    elif N==1:
        s[1]+=1
        return 1
    else:
        if cache[N] != -1:
            return cache[N]
        cache[N]=fibo(N-1)+fibo(N-2)

    return cache[N]

n=int(input())
for _ in range(n):
    s={0:0,1:0}
    m=int(input())
    fibo(m)
    print(*list(s.values()))