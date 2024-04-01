def solution(dartResult):
    answer = []
    num = ''
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i.isalpha():
            if i == "D":
                answer.append(int(num) ** 2)
            elif i == "T":
                answer.append(int(num) ** 3)
            else:
                answer.append(int(num))
            num = ''
        else:
            if i == "*":
                if len(answer) >= 2:
                    answer[-2] *= 2
                answer[-1] *= 2
            else:  # i == "#"
                answer[-1] *= -1

    return sum(answer)


print(solution("1D2S#10S"))
