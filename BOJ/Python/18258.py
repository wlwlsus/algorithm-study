import sys
from collections import deque

q=deque()
n=int(sys.stdin.readline())
for _ in range(n):
    try:
        m=sys.stdin.readline().split()
        if m[0]=='push':
            q.append(int(m[1]))
        elif m[0]=='pop':
            print(q.popleft())
        elif m[0]=='size':
            print(len(q))
        elif m[0]=='empty':
            if len(q)>0: print(0)
            else: print(1)
        elif m[0]=='front':
            print(q[0])
        elif m[0]=='back':
            print(q[-1])
    except IndexError:
        print(-1)