# from collections import deque

# n,m,v=map(int,input().split())
# s = [[0] * (n + 1) for i in range(n + 1)]
# for i in range(m):
#     x,y = map(int,input().split())
#     s[x][y]=s[y][x]=1
# visit=[0]*(n+1)


# def dfs(root):
#     visit[root]=1 #방문한 점 1로 표시
#     print(root, end=' ')
#     for i in range(1,n+1):
#         if(visit[i]==0 and s[root][i]==1):
#             dfs(i)

# def bfs(root):
#     d=deque([root])
#     visit[root]=0
#     while d:
#         now=d.popleft()
#         print(now,end=' ')
#         for i in range(1, n+1):
#             if visit[i]==i and s[now][i]==1:
#                 d.append(i)
#                 visit[i]=0

# print(dfs(v))
# # print()
# # print(bfs(v))

N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0


dfs(V)
print(1)
bfs(V)