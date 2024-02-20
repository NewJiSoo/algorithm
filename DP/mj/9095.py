# https://www.acmicpc.net/problem/9095
# 메모리 : 31120 KB, 시간 : 40 ms

T = int(input())


for _ in range(T):
    n = int(input())
    memo = [0] * (n+1)

    for i in range(1, n+1):
        if i == 1:
            memo[1] = 1
        elif i == 2:
            memo[2] = 2
        elif i == 3:
            memo[3] = 4
        else:
            memo[i] = memo[i-1]+memo[i-2]+memo[i-3]
    print(memo[n])
