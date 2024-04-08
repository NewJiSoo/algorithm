from collections import deque


def solution(priorities, location):
    answer = 0

    arr = deque()
    for idx, item in enumerate(priorities):
        arr.append((idx, item))

    while arr:
        x = arr.popleft()
        # 중요도가 낮으면 맨 뒤로 보내기
        if any(x[1] < i[1] for i in arr):
            arr.append(x)
        # 중요도가 높으면 뺀 상태로 나두긴
        else:
            answer += 1
            if x[0] == location:
                break

    return answer
