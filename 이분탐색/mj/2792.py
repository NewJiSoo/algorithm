# https://www.acmicpc.net/problem/2792
# 메모리 : 42876 KB, 시간 : 2288 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]

# 보석 (최소 1개) ~ (최대 같은 색깔 보석 수 중 가장 큰수)
start = 1
end = max(arr)

while start <= end:
    mid = (start+end)//2

    cnt = 0
    for num in arr:
        cnt += (num//mid)
        if num % mid > 0:
            cnt += 1

    # cnt가 더 크다는 것은 N명보다 많은 사람이 보석을 가져갔다는 것
    # 보석 수를 늘려서 가져가는 사람이 적어지도록 해야 함
    if cnt > N:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)
