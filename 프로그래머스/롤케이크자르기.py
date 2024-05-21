def solution(topping):
    answer = 0
    left = {}
    right = {}
    for x in topping:
        if x in right:
            right[x] += 1
        else:
            right[x] = 1

    right_count = len(right)
    for i in topping:
        if i not in left:
            left[i] = True

        if right[i] == 1:
            right_count -= 1
        right[i] -= 1

        if len(left) == right_count:
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
