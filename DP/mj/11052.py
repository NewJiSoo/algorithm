# https://www.acmicpc.net/problem/11052
# 메모리 : 31120 KB, 시간 : 208 ms

N = int(input())

p = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j]+dp[i-j])

print(dp[N])
