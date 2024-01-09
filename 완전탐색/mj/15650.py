# https://www.acmicpc.net/problem/15650
# 메모리 : 31120 KB, 시간 : 40 ms

N, M = map(int, input().split())


def backtrack(start, curr):
    if len(curr) == M:
        print(' '.join(map(str, curr)))
        return
    for i in range(start, N+1):
        curr.append(i)
        backtrack(i+1, curr)
        curr.pop()


backtrack(1, [])
