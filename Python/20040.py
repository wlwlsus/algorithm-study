import sys

r = sys.stdin.readline
n, m = map(int, r().split())
parent = [i for i in range(n)]
game = [list(map(int, r().split())) for _ in range(m)]


def find(target):
    if target == parent[target]:
        return target

    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a
    return False


result = 0
for i in range(m):
    x, y = game[i]
    if union(x, y):
        result = i + 1
        break

print(result)
