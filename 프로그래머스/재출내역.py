def solution(skill, skill_trees):
    answer = 0
    dic = {skill[i]: i for i in range(len(skill))}

    for skill_tree in skill_trees:
        idx = 0
        is_valid = True

        for s in skill_tree:
            if s in dic:
                if dic[s] == idx:
                    idx += 1
                else:
                    is_valid = False
                    break
        if is_valid:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
