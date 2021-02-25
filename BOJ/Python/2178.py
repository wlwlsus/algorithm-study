from collections import deque
n,m=map(int,input().split())

matrix=[list(map(int, input())) for _ in range(n)]
step = [[0]*m for _ in range(n)]
step[0][0]=1
dx,dy=[1,-1,0,0],[0,0,1,-1]

def bfs(col, row):
    matrix[col][row] = 0
    queue = deque([(col,row)])
    # global step
    
    while queue:
        col,row = queue.popleft()
        for k in range(4):
            nx = col + dx[k]
            ny = row + dy[k]
            if 0<= nx< n and 0<= ny < m:
                if matrix[nx][ny]==1 :
                    matrix[nx][ny]=0
                    step[nx][ny] = step[col][row] + 1
                    queue.append((nx, ny))

bfs(0,0)
print(step[n-1][m-1])