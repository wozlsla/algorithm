"""
문제 설명:
N x M 크기의 미로가 주어집니다. 미로는 0과 1로 구성되어 있으며, 0은 이동할 수 없는 벽을 나타내고, 1은 이동할 수 있는 경로를 나타냅니다.
시작 위치는 (0, 0)이며, 미로의 출구는 (N-1, M-1)에 위치해 있습니다.
최단 경로로 미로를 탈출하는 방법을 찾는 프로그램을 작성하세요. 이동은 상하좌우로만 가능합니다.
"""

"""
BFS를 사용하여 모든 가능한 경로를 탐색합니다.
각 단계에서 상하좌우로 이동할 수 있는지 확인하고, 가능하다면 해당 위치로 이동합니다.
출구에 도달했을 때의 경로 길이를 최소 경로 길이와 비교하여 업데이트합니다.
방문한 위치는 다시 방문하지 않도록 처리합니다.
"""

from collections import deque


def maze_bfs(map):

    n = len(map)
    m = len(map[0])

    # 이동 방향 (상, 하, 좌, 우)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 방문 여부를 확인하기 위한 배열
    visited = [[False] * m for _ in range(n)]

    # BFS
    queue = deque([(0, 0, 1)])  # x, y, !현재까지 이동 거리!
    visited[0][0] = True  # 시작점

    while queue:
        x, y, dist = queue.popleft()

        # 출구 도달
        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and map[nx][ny] == "1"
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 출구에 도달할 수 없는 경우
    return -1


# 입력
map = [
    "11101",
    "10101",
    "10101",
    "11111",
]

print(maze_bfs(map))
