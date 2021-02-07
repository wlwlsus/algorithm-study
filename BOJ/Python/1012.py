# t=int(input())
# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def dfs(x,y):
#     # global bug
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if(0<=nx<n and 0<=ny<m):
#             # if(matrix[nx][nx] == 1 and visited[nx][nx]==0):
#                 # visited[x][y]=1
#             if matrix[nx][ny] == 1: 
#                 matrix[nx][ny] = 0
#                 dfs(nx,ny)


# for _ in range(t):
#     m,n,k=map(int,input().split())
#     matrix=[[0]*m for _ in range(n)]
#     visited=[[0]*m for _ in range(n)]
#     bug=0

#     for i in range(k):
#         x,y=map(int,input().split())
#         matrix[y][x]=1

#     for i in range(n):
#         for j in range(m):
#             # if(matrix[i][j] == 1 and visited[i][j]==0):
#             if(matrix[i][j] == 1):
#                 print(f'현재 상태 {matrix}')
#             # if matrix[i][j] > 0: 
#                 dfs(i,j)
#                 bug+=1

#     print(bug)


for r in[0]*int(input()):
 d={(*map(int,input().split()),)for _ in[0]*int(input().split()[2])}
 while d:
  s=[d.pop()];r+=1
  while s:
   x,y=s.pop()
   for e in-2,0,2,4:
    p=x+e//3,y+e%3-1
    if{p}<=d:d-={p};s+=p,
 print(r)