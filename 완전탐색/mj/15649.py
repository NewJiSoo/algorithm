# https://www.acmicpc.net/problem/15649
# 메모리 : 31120 KB, 시간 : 164 ms

# 1부터 N까지 중복없이 M개 고른 수열

N, M = map(int, input().split())

ans = []


def backtrack(curr):
    if len(curr) == M:
        print(' '.join(map(str, curr)))
        return
    for num in range(1, N+1):
        if num not in curr:
            curr.append(num)
            backtrack(curr)
            curr.pop()


backtrack([])
