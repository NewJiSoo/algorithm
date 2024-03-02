# https://www.acmicpc.net/problem/11000
# 메모리 : 288376 KB, 시간 : 8736 ms
# 참고코드 : https://hongcoding.tistory.com/79

import heapq

N = int(input())

p = [] * N

for _ in range(N):
    s, t = list(map(int, input().split()))
    p.append([s, t])
p.sort()

room = []
heapq.heappush(room, p[0][1])  # t(끝나는 시간)만 넣기

for i in range(1, N):
    if p[i][0] < room[0]:  # 첫번째를 제외한 강의 시작시간이 첫번째 강의 끝나는 시간보다 작을 때
        # 새로운 강의실을 배정한다. (시작시간이 더 빠르기 때문에 i번째 강의를 이어서 할 수 없음)
        heapq.heappush(room, p[i][1])
    else:  # 강의 시작시간보다 끝나는 시간이 더 늦을 때
        heapq.heappop(room)  # 강의실은 그대로 하고 새로운 강의 시간으로 변경
        heapq.heappush(room, p[i][1])

print(len(room))
