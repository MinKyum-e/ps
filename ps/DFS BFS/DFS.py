

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for vertex in graph[v]:
        if visited[vertex] == False:
            dfs(graph, vertex, visited)


graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
        ]

visited = [False] * 9

dfs(graph, 1, visited)
