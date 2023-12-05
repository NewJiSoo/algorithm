memo = {}


def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)

    return memo[n]
