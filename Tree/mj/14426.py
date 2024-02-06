# https://www.acmicpc.net/problem/14426
# 시간초과

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

w_list = [input().rstrip() for _ in range(N)]

cnt = 0
for _ in range(M):
    S = input().rstrip()
    for i in w_list:
        if S[0] != i[0]:
            break
        if S == i[:len(S)]:
            cnt += 1
            break

print(cnt)
