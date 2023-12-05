from collections import deque


def bfs(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


bfs(graph, 'A')  # 시작점 : A,

# (미로 찾기 / 최단거리 문제)
