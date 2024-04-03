def solution(data, ext, val_ext, sort_by):
    answer = []

    for i in data:
        if ext == "date":
            if val_ext > i[1]:
                answer.append(i)
        elif ext == "maximum":
            if val_ext > i[2]:
                answer.append(i)
        elif ext == "remain":
            if val_ext > i[3]:
                answer.append(i)
        else:
            if val_ext > i[0]:
                answer.append(i)

    def sort_what(what):
        if what == "date":
            return sorted(answer, key=lambda x: x[1])
        elif what == "maximum":
            return sorted(answer, key=lambda x: x[2])
        elif what == "remain":
            return sorted(answer, key=lambda x: x[3])
        else:
            return sorted(answer, key=lambda x: x[0])
    answer = sort_what(sort_by)

    return answer


print(solution([[1, 20300104, 100, 80], [
      2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501,	"remain"))
