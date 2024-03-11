# https://www.acmicpc.net/problem/16401
# 메모리 : 143128 KB, 시간 : 3368 ms

M, N = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)
ans = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in arr:
        cnt += (i//mid)

    # 사람 수보다 나눌 수 있는 횟수가 더 많은 경우 -> 과자 길이를 늘려 나눌 수 있는 횟수를 줄이기
    if cnt >= M:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)
