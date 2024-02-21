# https://www.acmicpc.net/problem/10844
# 메모리 : 31120 KB, 시간 : 48 ms

n = int(input())

# dp[i][j]: 길이가 i이고 마지막 자릿수가 j인 계단 수의 개수
dp = [[0]*10 for _ in range(n+1)]


# 길이가 1인 경우
for i in range(1, 10):
    dp[1][i] = 1


# 길이가 2 이상인 경우
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
