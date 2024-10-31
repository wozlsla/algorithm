""" DFS """


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


""" BFS """


from collections import deque


def bfs_queue(graph, st):
    visited = []  # 방문한 노드
    deq = deque([st])  # 방문할 노드

    while deq:
        node = deq.popleft()  # 방문할 노드를 꺼내옴
        visited.append(node)

        for adj in graph[node]:  # 노드의 인접 순차 탐색
            if adj not in visited:
                deq.append(adj)

    return visited


""" Binary Search
1. 처음/끝을 잡는다
2. 중간값을 찾는다
3. 중간값과 타겟을 비교한다
4. 작으면 왼쪽, 크면 오른쪽으로 업데이트한다
(반복)
 """


def binary_search(nums, target):

    def bs(st, ed):
        if st > ed:
            return -1

        mid = (st + ed) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bs(st, mid - 1)
        elif nums[mid] < target:
            return bs(mid + 1, ed)

    return bs(0, len(nums) - 1)


"""
target = 4

[-1, 0, 3, 5, 9, 12]
 0      |         5 -> 5//2=2

[5, 9, 12]
 3  |   5 -> 8/2=4

[5] --> 같아짐 !!
"""
