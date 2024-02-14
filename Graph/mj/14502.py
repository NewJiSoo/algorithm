# https://www.acmicpc.net/problem/14502
# 메모리 : 125952 KB, 시간 : 2448 ms, pypy
# 참고 코드 : https://jie0025.tistory.com/209

import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs():
    # 바이러스 위치 담기(q)
    q = deque()
    # 바이러스 전파 테스트할 그래프 복사
    test_map = copy.deepcopy(graph)

    # 바이러스 찾기, 찾은 바이러스 q에 넣기
    for i in range(N):
        for k in range(M):
            if test_map[i][k] == 2:
                q.append((i, k))

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 바이러스 위치에서 위,아래,왼쪽,오른쪽이 0이라면 바이러스(2)로 변경
    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in direction:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if next_r >= 0 and next_r < N and next_c >= 0 and next_c < M:
                if test_map[next_r][next_c] == 0:
                    test_map[next_r][next_c] = 2
                    q.append((next_r, next_c))

    # 안전지역(0) 찾기(cnt) + 다른 곳에 벽을 세웠을 때 나왔던 안전지역 숫자와 비교(result)
    global result
    cnt = 0
    for i in range(N):
        for k in range(M):
            if test_map[i][k] == 0:
                cnt += 1
    result = max(result, cnt)


# 벽 세우기
def make_wall(cnt):
    if cnt == 3:
        bfs()  # 벽다세웠으면 바이러스 확인
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)  # 벽이 3개가 될 때까지 반복
                graph[i][j] = 0  # 원래대로 되돌리기


result = 0
make_wall(0)
print(result)
