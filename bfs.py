def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        # print(f'현재 q의 상태 : {queue}')
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            print(f'그래프 노트 : {graph[node]}')
            queue.extend(graph[node])

    return visit

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))