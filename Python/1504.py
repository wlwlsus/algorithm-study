import sys
import heapq

r = sys.stdin.readline
n, e = map(int, r().split())
INF = sys.maxsize

graph = [[] for i in range(n+1)]

for _ in range(e):
    a, b, c = map(int, r().split())
    # 양방향 그래프
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, r().split())


def dij(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        for new_node, new_dist in graph[current_node]:
            new_dist += current_dist
            if new_dist < dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(queue, [new_dist, new_node])
    return dist


# (1 - v1 - v2 - n), (1 - v2 - v1 - n) 두 가지 경로를 가지므로 둘 중에 최소 값을 선택
# 없으면 INF
t1 = dij(1)
t2 = dij(v1)
t3 = dij(v2)

m = min(t1[v1] + t2[v2] + t3[n], t1[v2] + t3[v1] + t2[n])

if m < INF:
    print(m)
else:
    print(-1)
