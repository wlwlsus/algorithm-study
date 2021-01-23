# Vector Setting
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = [(x,y)]

    o, v = 0, 0
    while queue:
        x, y = queue.pop()
        if field[x][y]=='v':
            v +=1
        if field[x][y]=='o':
            o +=1

        field[x][y]='#'

        # 모든 방향(상하좌우) 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N :       # x 범위가 r, y범위가 c 안넘게
                if field[nx][ny] != '#':
                    queue.append((nx,ny))          # v, o 발견 시 queue 추가 
                   
    if o<=v :
        o = 0
    else:
        v = 0
    return o, v
  
M, N = map(int, input().split())
field = [list(input()) for _ in range(M)]
O, V = 0, 0
for i in range(M):
    for j in range(N):
        if field[i][j]=='v' or field[i][j]=='o':    #양, 늑대 발견 시 BFS 탐색
            o, v = bfs(i,j)
            O +=o
            V +=v
 
print(O, V)