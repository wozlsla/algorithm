""" DFS """

from structures import dfs_recursive, dfs_stack

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9],
}

assert dfs_recursive(graph, 1, []) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert dfs_stack(graph, 1) == [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]


from DFS_island import island_dfs_stack, island_dfs_recursive

assert (
    island_dfs_stack(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    == 1
)
assert (
    island_dfs_stack(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    == 3
)

assert (
    island_dfs_recursive(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    == 1
)
assert (
    island_dfs_recursive(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    == 3
)


""" BFS """
from BFS_island import island_bfs

assert (
    island_bfs(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    == 1
)
assert (
    island_bfs(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    == 3
)


""" Binary Search """
from structures import binary_search

assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
