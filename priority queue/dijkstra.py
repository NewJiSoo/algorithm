import heapq


def dijkstra(graph, start, final):
    costs = {}  # 비용 덱, {노드:최소 비용의 합}
    pq = []  # 우선순위 큐 리스트
    heapq.heappush(pq, (0, start))  # 시작 노드, 비용 넣기

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)  # pq리스트에 가장 우선순위가 높은 비용, 노드 꺼내기
        if cur_v not in costs:  # 방문한 적이 없다면 = 최소 비용의 합을 저장한 적이 없다면
            costs[cur_v] = cur_cost  # 노드에 최소비용 저장
            for cost, next_v in graph[cur_v]:  # 현재 노드와 이어진 다음 노드들 꺼내서 pq에 넣기
                next_cost = cur_cost + cost  # 다음 노드의 비용 = 현재 누적된 비용 + 기존 노드 비용
                heapq.heappush(pq, (next_cost, next_v))  # 우선순위 큐에 다음 노드 집어넣기
        return costs[final]  # 최종 노드에 도착하는 비용 반환


# 가중치 그래프 (비용, 노드)
graph = {
    # 1번 노드와 연결된 노드 : 2, 4번, 2번 노드로 가는 비용 : 2, 4번 노드로 가는 비용 : 1
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    # ...
}

dijkstra(graph, 1, 8)  # 시작: 1, 도착 : 8
