import heapq


n, m = map(int, input().split())
start = int(input())

# graph = {node: float('Inf') for node in range(1, n+1)}
graph = [[] for i in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    # graph[u] = {v: w}
    graph[u].append([v, w])
distances = [float('inf')] * (n + 1)
# print(graph)
# print(distances)

def dijkstra(graph, start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 탐색할 거리, 노드
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드가 거리가 기존에 있는 거리보다 멀다면 pass
        if distances[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리

            if distance < distances[new_node]:  # 알고 있는 거리보다 작으면 갱신
                distances[new_node] = distance
                # 다음 인접 거리를 계산하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_node])

    return distance

print(dijkstra(graph, 1))