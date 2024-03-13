# https://www.acmicpc.net/problem/15810
# 메모리 : 144340 KB, 시간 : 3560 ms

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 1
end = max(A)*M

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in A:
        cnt += (mid//i)

    # 만드려는 풍선 수 보다 더 많이 만들게 될 경우 시간을 줄인다.
    if cnt >= M:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
