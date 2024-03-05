# https://www.acmicpc.net/problem/6603
# 메모리 : 31120 KB, 시간 : 44 ms

def backtrack(start, curr):
    if len(curr) == 6:
        print(*curr)
        return

    for i in range(start, k):
        curr.append(S[i])
        backtrack(i+1, curr)
        curr.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    backtrack(0, [])

    if k == 0:
        exit()
    print()
