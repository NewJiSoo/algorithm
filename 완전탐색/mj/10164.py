# https://www.acmicpc.net/problem/10164
# 메모리 : 31120 KB, 시간 : 44 ms
# 참고 코드 : https://velog.io/@rlvy98/%EB%B0%B1%EC%A4%8010164.-%EA%B2%A9%EC%9E%90%EC%83%81%EC%9D%98-%EA%B2%BD%EB%A1%9Cpython-%ED%8C%8C%EC%9D%B4%EC%8D%AC

N, M, K = map(int, input().split())


def search(n, m):
    dp = [[0]*(m+1)] * (n+1)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][m]


if K:
    row_k = (K-1)//M + 1
    col_k = K - M*(row_k-1)

    row_k2 = N - (row_k-1)
    col_k2 = M - (col_k-1)

    ans1 = search(row_k, col_k)
    ans2 = search(row_k2, col_k2)
    print(ans1*ans2)
else:
    print(search(N, M))
