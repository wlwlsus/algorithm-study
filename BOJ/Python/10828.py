import sys
n=int(sys.stdin.readline().rstrip());s=[]
for _ in range(n):
    i=input()
    if i.__contains__("push"):
        v= list(map(str,i.split()))[1]
        s.append(v)
    elif i=='top':
        if s:print(s[-1])
        else:print(-1)
    elif i=='size':
        print(len(s))
    elif i=='empty':
        if not s:print(1)
        else:print(0)
    elif i=='pop':
        if s:
            s.pop()
        else:print(-1)