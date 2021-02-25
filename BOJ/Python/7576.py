from collections import deque

n,m=map(int,input().split())
matrix = [ list(map(int,input().split())) for _ in range(m) ]
day = [[0]*n for _ in range(m)]

dx, dy = [1,-1,0,0],[0,0,1,-1]

def bfs(col, row):
    day[col][row] = 0
    days=-1

    while queue:
        col,row = queue.popleft()
        for k in range(4):
            nx = col + dx[k]
            ny = row + dy[k]

            if 0<=nx<m and 0<=ny<n:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = -1
                    day[nx][ny] = day[col][row] + 1
                    queue.append([nx,ny])

queue=deque()
for i in range(m):
    print(matrix[i])            
    for j in range(n):
        if matrix[i][j]==1:
            queue.append([i,j])

# bfs(m-1,n-1)
# for i in day:
#     # if 0 in i:
#     #     print(-1)
#     print(*i)