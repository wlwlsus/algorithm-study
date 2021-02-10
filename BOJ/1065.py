n=int(input())

def han(N):
    c = 0
    if N<100:
        return N
    else:
        for i in range(100, N+1):
            a = list(map(int,str(i)))
            if(a[0]-a[1]==a[1]-a[2]):
                c += 1
        return 99+c   

print(han(n))