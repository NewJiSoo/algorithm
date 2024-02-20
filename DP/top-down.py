memo = {}  # memo에 저장함으로써 재사용
# memo = { 1:1, 2:2 }


def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)  # 재귀를 이용

    return memo[n]
