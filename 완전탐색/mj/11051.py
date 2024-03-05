# https://www.acmicpc.net/problem/11051
# 메모리 : 31120 KB, 시간 : 44 ms

N, K = map(int, input().split())


def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res


result = factorial(N)//(factorial(K)*factorial(N-K))

print(result % 10007)
