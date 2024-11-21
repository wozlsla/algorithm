# Heap : 방문해야 할 노드들 + 그에 이르는 누적 비용(최소값)이 있는 목록
import heapq


def dijkstra(graph, start):
    INF = 1e9
    dist = [INF] * len(graph)  # 비용

    dist[start] = 0
    q = []

    # 쌍으로 넣어주면 idx 0을 기준으로 최소힙 구성
    heapq.heappush(q, (0, 1))  # (누적비용, 노드번호)

    # 방문할 노드가 남아있으면
    while q:
        acc, node = heapq.heappop(q)

        if acc > dist[node]:
            continue

        dist[node] = acc  # update
        for next, cost in graph[node]:
            new_cost = acc + cost
            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(q, (new_cost, next))

    return dist
