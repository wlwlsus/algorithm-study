import sys
input = sys.stdin.readline

N = int(input())
li=dict()
for _ in range(N):
    name = input().rstrip()
    if(name in li):
        li[name] += 1
    else:
        li[name]=1

for i in range(N-1):
    name = input().rstrip()
    li[name] -= 1

for j in li:
    if li[j]: #1개 이상 걸름
        print(j)
        break