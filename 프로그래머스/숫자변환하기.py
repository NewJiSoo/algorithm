from collections import deque


def solution(x, y, n):
    if x == y:
        return 0
    dic = {}
    q = deque([(x, 0)])

    while q:
        cur, step = q.popleft()

        for v in [cur*3, cur*2, cur+n]:
            if v == y:
                return step+1

            if v not in dic and v <= y:
                dic[v] = step + 1
                q.append((v, step+1))

    return -1


print(solution(10, 40, 5))
