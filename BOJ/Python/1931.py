import sys
n=int(sys.stdin.readline())
s=[]
# arr1=list(map(int,sys.stdin.readline().split()))
cnt=1
for i in range(n):
    s.append(tuple(map(int,sys.stdin.readline().split())))

s.sort(key=lambda x:(x[1],x[0]))
t1=s[0]

for i in range(1,n):
    t2=s[i]
    if t1[1]<=t2[0]:
        t1=t2
        cnt+=1

print(cnt)