# https://www.acmicpc.net/problem/2470
# 메모리 : 42036 KB, 시간 : 128 ms

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
start = 0
end = N-1

ans = [arr[start], arr[end]]  # 정답 넣을 배열

while start < end:
    total = arr[start]+arr[end]

    # 더 작은 합들이 있으면 바꾸기
    if abs(ans[0]+ans[1]) > abs(total):
        ans[0] = arr[start]
        ans[1] = arr[end]

    if total > 0:
        end -= 1
    else:
        start += 1

print(*ans)
