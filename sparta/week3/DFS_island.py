def island_dfs_stack(grid):
    """
    grid[r][c]

    grid[r-1][c] 상
    grid[r+1][c] 하
    grid[r][c-1] 좌
    grid[r][c+1] 우
    """

    # 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 경계값
    rows = len(grid)
    cols = len(grid[0])

    cnt = 0  # 섬의 개수

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            cnt += 1

            stack = [(r, c)]  # 방문해야 할 노드들
            while stack:
                x, y = stack.pop()
                grid[x][y] = "0"

                for i in range(4):
                    nr = x + dr[i]
                    nc = y + dc[i]

                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or grid[nr][nc] != "1"
                    ):
                        continue

                    stack.append((nr, nc))

    return cnt


def island_dfs_recursive(grid):
    cnt = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs_recursive(r, c):
        grid[r][c] = "0"  # 방문 처리
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != "1":
                continue

            dfs_recursive(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt
