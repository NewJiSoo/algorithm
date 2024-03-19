def solution(name, yearning, photo):
    answer = []
    people = {name[i]: yearning[i] for i in range(len(name))}
    for to in photo:
        cnt = 0
        for pho in to:
            if pho in people:
                cnt += people[pho]
        answer.append(cnt)

    return answer
