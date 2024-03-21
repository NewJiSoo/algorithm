def solution(s, skip, index):
    answer = ''
    for char in s:
        cnt = 0
        new_ord = ord(char)
        while index != cnt:
            new_ord += 1
            if new_ord > ord('z'):
                new_ord = new_ord - ord('z') + ord('a') - 1
            if chr(new_ord) in skip:
                continue
            else:
                cnt += 1

        answer += chr(new_ord)

    return answer


print(solution("aukks", "wbqd", 5))  # 정답 : "happy"
