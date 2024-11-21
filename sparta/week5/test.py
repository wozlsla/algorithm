import os
import sys
from dijkstra import dijkstra

with open(f"{os.getcwd()}/sparta/week5/dijkstra_testcase.txt") as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())  # 노드, 간선 개수
    start = int(input())
    graph = [[] for _ in range(n + 1)]  # 0 번째 노드를 쓰기 않기 때문

    for _ in range(m):  # 간선 개수만큼 반복
        a, b, c = map(int, input().split())
        graph[a].append((b, c))  # b:목적지, c:비용

assert dijkstra(graph, start) == [1000000000, 0, 8, 9, 5, 7]
# 1000000000: 0번째 노드로 가는 비용. 0번째는 쓰지 않기 때문에 무시
