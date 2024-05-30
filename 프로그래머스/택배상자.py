from collections import deque


def solution(order):
    answer = 0
    q = deque(order)
    stack = []
    idx = 1

    while idx <= len(order):
        if q and q[0] == idx:
            answer += 1
            idx += 1
            q.popleft()
        elif stack and stack[-1] == q[0]:
            answer += 1
            q.popleft()
            stack.pop()
        else:
            stack.append(idx)
            idx += 1

    while q and stack and stack[-1] == q[0]:
        answer += 1
        q.popleft()
        stack.pop()

    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
