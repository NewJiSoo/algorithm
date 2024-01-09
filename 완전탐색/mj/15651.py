# https://www.acmicpc.net/problem/15650
# 메모리 : 31120 KB, 시간 : 1392 ms

N, M = map(int, input().split())


def backtrack(curr):
    if len(curr) == M:
        print(' '.join(map(str, curr)))
        return

    for i in range(1, N+1):
        curr.append(i)
        backtrack(curr)
        curr.pop()


backtrack([])
