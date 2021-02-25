n=int(input())
m=[list(map(int, input())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
label=1
house = 0
house_list =[]


def dfs(col,row,):
    global house
    visited[col][row]=1
    if m[col][row] == 1 :
        house +=1

    for x in range(4):
        nx = col + dx[x]
        ny = row + dy[x]

        if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and m[nx][ny]==1:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if m[i][j]==1 and visited[i][j]==0:
            dfs(i,j)
            house_list.append(house)
            house=0

print(len(house_list))
for k in  sorted(house_list):
    print(k)