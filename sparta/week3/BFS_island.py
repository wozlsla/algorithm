from collections import deque


def island_bfs(grid):
    cnt = 0

    rows = len(grid)
    cols = len(grid[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            cnt += 1
            deq = deque([(r, c)])  # 방문할 곳

            while deq:
                # 1. 방문처리
                # 2. 인접 노드 방문 예약

                x, y = deq.popleft()  # node
                grid[x][y] = "0"

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (
                        nx < 0
                        or nx >= rows
                        or ny < 0
                        or ny >= cols
                        or grid[nx][ny] != "1"
                    ):
                        continue

                    deq.append((nx, ny))
    return cnt
