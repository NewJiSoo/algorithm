def solution(today, terms, privacies):
    answer = []
    year, month, day = today.split(".")
    year = int(year)
    month = int(month)
    day = int(day)

    term = {}
    for i in terms:
        a, b = i.split()
        term[a] = int(b)

    for i in range(len(privacies)):
        n, t = privacies[i].split()
        y, m, d = n.split(".")
        y = int(y)
        m = int(m)
        d = int(d) - 1
        if d < 1:
            m -= 1
            d = 28
            if m < 1:
                y -= 1
                m = 12

        ex = term[t] + m
        if ex > 12:
            y += ex//12
            ex = ex % 12
            if ex == 0:
                ex = 12
                y -= 1

        if year > y or (year >= y and month > ex) or (year >= y and month >= ex and day > d):
            answer.append(i+1)
    return answer


print(solution("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]))
