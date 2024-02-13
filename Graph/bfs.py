from collections import deque


def bfs(graph, start_v):
    visited = [start_v]  # 방문 목록에 시작점 넣기
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)  # 방문 하고
                queue.append(v)  # queue에 예약 넣어주기
    return visited


graph = {
    "A": ["B"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "E", "F"],
    "E": ["B", "D",  "F"],
    "F": ["D", "E"],
}

bfs(graph, 'A')

# (미로 찾기 / 최단거리 문제)
