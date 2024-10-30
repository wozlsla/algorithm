def dfs_recursive(graph, node, visited):
    visited.append(node)

    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited


def dfs_stack(graph, st):
    visited = []  # 방문한 목록
    stack = []  # 방문해야 하는 목록

    while stack:
        node = stack.pop()
        visited.append(node)

        for adj in graph[node]:
            if adj not in visited:
                stack.append(adj)

    return visited
