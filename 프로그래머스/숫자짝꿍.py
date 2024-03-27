def solution(X, Y):
    answer = ''
    arr = []
    X_sorted = sorted(X, reverse=True)
    Y_dic = {}

    for i in Y:
        if i in Y_dic:
            Y_dic[i] += 1
        else:
            Y_dic[i] = 1

    for char in X_sorted:
        if char in Y_dic and Y_dic[char] > 0:
            arr.append(char)
            Y_dic[char] -= 1

    if arr:
        if arr[0] == "0":
            return "0"
        answer = ''.join(arr)
    else:
        answer = "-1"

    return answer


print(solution("100", "203045"))
