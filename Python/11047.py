n, v = map(int, input().split())
c=[int(input()) for _ in range(n)]
# c.reverse()
cnt=0

#-i 가 마지막 인덱스여야하므로 range(1, n+1)
for i in range(1,n+1):
    i=c[-i]
    if(v>=i):
        cnt+=v//i
        v=v-(v//i*i)

print(cnt)