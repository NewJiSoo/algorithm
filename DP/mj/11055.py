# https://www.acmicpc.net/problem/11055
# 메모리 : 31120 KB, 시간 : 44 ms

A = int(input())
A_list = list(map(int, input().split()))

dp = [0]*A
dp[0] = A_list[0]

for i in range(A):
    for j in range(A):
        if A_list[i] < A_list[j]:
            dp[i] = max(dp[i], dp[j]+A_list[i])
        else:
            dp[i] = max(dp[i], A_list[i])
