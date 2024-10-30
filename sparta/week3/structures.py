def dfs_recursive(graph, node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited


def dfs_stack(graph, st):
    visited = []  # 방문한 목록
    stack = [st]  # 방문해야 하는 목록

    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리
        node = stack.pop()
        visited.append(node)

        # 인접 노드를 방문한다.
        for adj in graph[node]:
            if adj not in visited:
                stack.append(adj)

    return visited
