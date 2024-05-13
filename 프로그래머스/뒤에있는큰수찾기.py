# 시간 복잡도 O(n)

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        # 스택이 비어있지 않고, 현재 숫자가 스택 top에 있는 인덱스의 숫자보다 큰 경우,
        # 해당 인덱스의 뒷 큰수가 현재 숫자이므로 answer 리스트에 현재 숫자를 저장
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)

    return answer


print(solution([9, 1, 5, 3, 6, 2]))
