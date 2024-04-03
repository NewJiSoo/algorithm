def solution(new_id):
    answer = ''
    by = ["-", "_", "."]

    # 1단계: 모든 대문자를 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 허용된 문자 이외의 문자 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in by:
            answer += i

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer.startswith("."):
        answer = answer[1:]
    if answer.endswith("."):
        answer = answer[:-1]

    # 5단계: 빈 문자열인 경우 "a"를 대입
    if not answer:
        answer = 'a'

    # 6단계: 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith("."):
            answer = answer[:-1]

    # 7단계: 길이가 2자 이하인 경우 마지막 문자를 반복해서 붙임
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


print(solution("1234567890.123.456"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("................b"))
