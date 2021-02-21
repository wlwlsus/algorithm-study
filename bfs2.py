from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    
    return visited

graph_list = {1:set([3,4]),
    2:set([3,4,5]),
    3:set([1,5]),
    4:set([1]),
    5:set([2,6]),
    6:set([3,5])
}
root_node =1

print(bfs(graph=graph_list, root=root_node))