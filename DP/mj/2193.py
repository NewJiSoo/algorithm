# https://www.acmicpc.net/problem/2193
# 메모리 : 31120 KB, 시간 : 40 ms

n = int(input())
if n == 1:
    print(1)
else:
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n - 1])
