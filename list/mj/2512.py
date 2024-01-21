# https://www.acmicpc.net/problem/2512
# 메모리 : 32140 KB, 시간 : 84 ms

import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start, end = 0, max(N_list)

while start <= end:
    total = 0
    mid = (start+end) // 2

    for i in N_list:
        # 요청한 금액(i)과 예산 상한액(mid) 비교해서 더 적은금액 넣기(상한액 이하의 예산 요청은 요청한 금액(i) 배정하기 때문)
        total += min(mid, i)

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
