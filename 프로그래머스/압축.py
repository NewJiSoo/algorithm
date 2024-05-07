
def solution(msg):
    answer = []
    dic = {chr(i): i - 64 for i in range(65, 91)}
    arr = [chr(i) for i in range(65, 91)]

    idx = 27  # 초기 사전에는 A부터 Z까지 26개의 문자가 있으므로 다음 인덱스는 27부터
    w = msg[0]  # 현재 처리 중인 문자열
    i = 1

    while i <= len(msg):
        c = msg[i] if i < len(msg) else ''  # 다음 글자
        if w + c in dic:  # w+c가 사전에 존재하는지 확인
            w += c  # 다음 글자도 사전에 존재하므로 w를 확장
        else:
            answer.append(dic[w])  # w에 해당하는 인덱스를 출력
            dic[w + c] = idx  # w+c를 사전에 추가
            idx += 1
            w = c  # 다음 글자부터 다시 시작
        i += 1
    answer.append(dic[w])

    return answer


print(solution('KAKAO'))  # [11, 1, 27, 15]
