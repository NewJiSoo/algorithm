# https://www.acmicpc.net/problem/14627
# 메모리 : 71112 KB, 시간 : 3588 ms

import sys
input = sys.stdin.readline

S, C = map(int, input().split())
L = [int(input()) for _ in range(S)]

start = 1
end = max(L)
ans = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in L:
        cnt += (i//mid)

    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1


total = sum(L) - ans*C
print(total)
