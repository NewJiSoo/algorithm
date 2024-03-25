def solution(t, p):
    answer = 0
    h = len(p)
    for i in range(len(t)):
        if i + h <= len(t):
            if int(t[i]) <= int(p[0]):
                if int(t[i:i+h]) <= int(p):
                    answer += 1

    return answer


print(solution("1221351118575141528544", "12511"))
