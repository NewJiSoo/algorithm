def solution(keymap, targets):
    dic = {}
    for q in range(len(keymap)):
        for w in range(len(keymap[q])):
            if keymap[q][w] in dic:
                dic[keymap[q][w]].append(w+1)
            else:
                dic[keymap[q][w]] = [w+1]

    answer = []
    for target in targets:
        result = 0
        for j in target:
            if j in dic:
                result += min(dic[j])
            else:
                result = -1
                break
        answer.append(result)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))  # 정답 [9, 4]
