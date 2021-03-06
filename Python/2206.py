from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(col, row):
    cnt = 1
    matrix[col][row] = 1
    queue = deque([(col, row)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    cnt += 1
                    matrix[nx][ny] = 1
                    queue.append([nx, ny])
    return cnt


print(bfs(0, 0))
