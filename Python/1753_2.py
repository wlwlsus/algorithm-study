import sys
import heapq

r = sys.stdin.readline
INF = float('inf')


def dijkstra(start, graph):
    # 최단 경로 리스트
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        for new_destination, new_distance in graph[current_destination]:
            new_distance += current_distance
            if new_distance < distances[new_destination]:
                distances[new_destination] = new_distance
                heapq.heappush(queue, [new_distance, new_destination])
    return distances


n, m = map(int, r().split())
start = int(r())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, r().split())
    graph[u].append([v, w])

for x in dijkstra(start, graph)[1:]:
    print(x if x != INF else "INF")
