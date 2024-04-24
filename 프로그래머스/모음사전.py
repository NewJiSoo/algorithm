def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    arr = []
    count = 0  # 마지막 5번째 자리에서 바뀌는 값

    while 1:
        if "".join(arr) == word:
            break

        answer += 1
        if len(arr) != 5:
            count = 0
            arr.append('A')

        elif len(arr) == 5 and arr[-1] == 'U':
            while arr[-1] == 'U':
                arr.pop()

            if alpha.index(arr[-1])+1 <= 4:
                # U를 모두삭제하고 마지막 값을 다음 값으로 변경한다
                arr[-1] = alpha[alpha.index(arr[-1])+1]
            else:
                arr[-1] = alpha[0]

        elif len(arr) == 5:
            count += 1
            arr[4] = alpha[count]

    return answer
