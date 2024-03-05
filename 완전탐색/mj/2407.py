# https://www.acmicpc.net/problem/2407
# 메모리 : 31120 KB, 시간 : 40 ms

n, m = map(int, input().split())


def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


result = fact(n) // (fact(m)*fact(n-m))

print(result)
