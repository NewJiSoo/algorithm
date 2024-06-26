def solution(numbers):
    def f(x):
        if x % 2 == 0:  # x가 짝수인 경우
            return x + 1
        else:  # x가 홀수인 경우
            # x의 이진 표현에서 가장 낮은 위치의 0을 1로 바꾸고
            # 그 뒤의 1을 0으로 바꾼다.
            # 예: 7 (0111) -> 11 (1011)
            bin_x = bin(x)[2:]  # x의 이진 문자열(0b제거)
            if '0' not in bin_x:  # 모든 비트가 1인 경우
                return int('10' + bin_x[1:], 2)  # 2진 문자열 10진수로 바꾸기
            else:
                zero_pos = bin_x.rfind('0')  # 0위치 찾기
                # 10넣고 그 자리에 있던 숫자 빼기
                return int(bin_x[:zero_pos] + '10' + bin_x[zero_pos+2:], 2)

    return [f(number) for number in numbers]


# 테스트
print(solution([2, 7]))  # 결과: [3, 11]
