def solution(id_list, report, k):
    answer = {}
    dic = {}
    for i in id_list:
        dic[i] = []
        answer[i] = 0

    new = list(set(report))

    # 사용자의 신고 내역을 딕셔너리에 저장
    for q in new:
        a, b = q.split()
        dic[b].append(a)

    for user in dic:
        if len(dic[user]) >= k:
            for name in dic[user]:
                answer[name] += 1
    res = list(answer.values())
    return res


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
