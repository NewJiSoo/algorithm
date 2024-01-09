# https://www.acmicpc.net/problem/15652
# 메모리 : 31120 KB, 시간 : 48 ms

N, M = map(int, input().split())


def backtrack(start, curr):
    if len(curr) == M:
        print(' '.join(map(str, curr)))
        return

    for i in range(start, N+1):
        curr.append(i)
        backtrack(i, curr)
        curr.pop()


backtrack(1, [])
