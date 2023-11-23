# https://www.acmicpc.net/problem/2606
# 메모리 : 34052 KB, 시간 : 76ms

from collections import deque

n = int(input())
m = int(input())
computer = [[] for _ in range(n + 1)]  # 컴퓨터 : 0번~n번

# 컴퓨터 쌍의 수 : m개
# 컴퓨터 0번부터 순서대로 -> [[], [2, 5], [1, 3], [2], [7], [1, 6], [5], [4]]
# 0번 컴퓨터는 존재하지 않음으로 비어있음
for i in range(m):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

# 방문 수 최대 : 컴퓨터 수 + 0번 컴퓨터(인덱스로 넣을 것이기 때문에 0번도 넣어줌)
visited = [False] * (n+1)

# 1번 컴퓨터 부터 시작


def bfs(start, visited):
    count = 0
    # visited : [[False], [True], [False], [False], [False], [False], [False]]
    visited[start] = True
    # queue : [[1]]
    queue = deque([start])
    while queue:  # queue에 컴퓨터가 존재할 때 까지 반복(완전 탐색)
        # cur_v : 방문할 컴퓨터
        cur_v = queue.popleft()

        for v in computer[cur_v]:
            # 방문하지 않았던 컴퓨터일 경우 = False일 경우
            if not visited[v]:
                # 방문 시 False -> True
                visited[v] = True
                # 다음 방문할 컴퓨터를 queue에 넣어줌
                queue.append(v)
                count += 1

    print(count)
    return count


bfs(1, visited)
