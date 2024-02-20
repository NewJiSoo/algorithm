# hhttps://www.acmicpc.net/problem/1463

N = int(input())

# bottom up
# 메모리 : 38932 KB, 시간 : 580ms
memo = [0] * (N+1)

for i in range(2, N+1):
    memo[i] = memo[i-1]+1  # i-1번 횟수 + 1을 해야 i번째 횟수가 된다
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1)


print(memo[N])


# top down
# 런타임에러
me = {}


def dp(n):
    if n == 1:
        return 0

    if n not in me:
        if n % 3 == 0 and n % 2 == 0:
            me[n] = min(dp(n//3)+1, dp(n//2)+1)
        if n % 3 == 0:
            me[n] = min(dp(n//3)+1, dp(n-1)+1)
        elif n % 2 == 0:
            me[n] = min(dp(n//2)+1, dp(n-1)+1)
        else:
            me[n] = dp(n-1)+1
    return me[n]


print(dp(N))
