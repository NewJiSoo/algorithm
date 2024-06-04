def solution(record):
    answer = []
    dic = {}
    result = []

    for i in record:
        cmd = i.split()

        if cmd[0] == 'Enter':
            result.append((0, cmd[1]))
            dic[cmd[1]] = cmd[2]

        elif cmd[0] == 'Leave':
            result.append((1, cmd[1]))

        elif cmd[0] == 'Change':
            dic[cmd[1]] = cmd[2]

    for j in result:
        if j[0] == 0:
            answer.append(dic[j[1]]+"님이 들어왔습니다.")
        elif j[0] == 1:
            answer.append(dic[j[1]]+"님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
