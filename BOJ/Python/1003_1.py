n=int(input())
for _ in range(n):
    zero=1
    one=0
    tmp=0
    m=int(input())
    for _ in range(m):
        tmp = one
        one = one+zero
        zero = tmp
    print(zero,one)