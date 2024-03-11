# 메모리 :  KB, 시간 :  ms

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


def fibo(n):
    if n == 1 or 2:
        return 1
    return fibo(n-1) + fibo(n-2)
