from collections import defaultdict
from collections import deque


def bfs(i):
    visited =[]
    queue = deque([i])

    while queue:
        next = queue.popleft()
        for x in graph[next]:
            if x not in visited:
                queue.append(x)
                visited.append(x)
    return len(visited)-1 

n = int(input())
k = int(input())
graph = defaultdict(list)
for i in range(k):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(bfs(1))