n,m = map(int,input().split())

li=[list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


count = 0
for i in li:
    for j in i:
        if(j==1):
            dfs()

def dfs():
    pass