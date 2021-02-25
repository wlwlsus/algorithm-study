# BOJ 7576 - 토마토
import sys
from collections import deque
r = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(M, N):
    days = -1

    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (matrix[nx][ny] == 0):
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])

    for b in matrix:
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())

queue = deque()
matrix = [ list(map(int,input().split())) for _ in range(N) ]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            # 익은 토마토 찾기 
            queue.append([i, j])

print(bfs(M, N))