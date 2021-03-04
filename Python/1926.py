from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
t = []


def bfs(col, row):
    matrix[col][row] = 0
    area = 1
    q = deque()
    q.append([col, row])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    area += 1
                    matrix[nx][ny] = 0
                    q.append([nx, ny])

    return area


cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt += 1
            t.append(bfs(i, j))

print(cnt)
if len(t):
    print(max(t))
else:
    print(0)
