from itertools import combinations

n, m = map(int, input().split())
total = list(combinations(range(1, n + 1), 3))
temp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    temp[x][y] = 1
    temp[y][x] = 1
    cnt = 0

for x in total:
    # 맛없는 조합에 1표시, 해당 조합은 pass
    if temp[x[0]][x[1]] or temp[x[0]][x[2]] or temp[x[1]][x[2]]:
        continue
    cnt += 1
print(cnt)
