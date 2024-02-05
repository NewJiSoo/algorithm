from collections import deque


def bfs(root):
    visited = []  # 방문기록(값 저장용 위해)
    if root is None:
        return 0
    q = deque()
    q.append(root)  # 시작 루트
    while q:
        cur_node = q.popleft()  # 접근/q에서 나온 노드
        visited.append(cur_node.value)  # 방문/값 저장

        if cur_node.left:  # 왼쪽 방문
            q.append(cur_node.left)
        if cur_node.right:  # 오른쪽 방문
            q.append(cur_node.right)
    return visited
