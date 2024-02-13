graph = {
    "A": ["B"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "E", "F"],
    "E": ["B", "D",  "F"],
    "F": ["D", "E"],
}

visited = []


def dfs(start):
    visited.append(start)  # 시작점 부터 방문하고
    for v in graph[start]:  # 시작점과 연결된 노드 찾기
        if v not in visited:  # 만약 그 노드가 방문이 안되있으면
            dfs(v)  # dfs 호출해서 방문하기


dfs('A')
