def solution(survey, choices):
    answer = ''
    dic = {}
    for d in ['RT', 'CF', 'JM', 'AN']:
        dic[d[0]] = 0
        dic[d[1]] = 0

    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            dic[survey[i][0]] += (4-choices[i])

    for j in ['RT', 'CF', 'JM', 'AN']:
        if dic[j[0]] < dic[j[1]]:
            answer += j[1]
        else:
            answer += j[0]

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
