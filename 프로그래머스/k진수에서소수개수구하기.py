def change(n, k):
    ternary = ''
    while n != 0:
        remainder = n % k
        ternary = str(remainder) + ternary
        n //= k
    return ternary


def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    number = str(change(n, k))
    for num in number.split('0'):
        if num and is_prime_number(int(num)):
            answer += 1

    return answer


# 진법 변환(10진법 제외)
# k진수로 변환하고 싶을 때
# 변환하고 싶은 숫자 n을 k로 나눈 후 나머지를 구한다
# 몫이 0이 될때 까지 나오는 나머지들을 거꾸로 나열한다

# 10진법 구하기
# 각 자리수를 해당 진법의 지수와 곱한다.
# 예) 201의 10진법은 (2 * 3^2) + (0 * 3^1) + (1 * 3^0) = 18 + 0 + 1 = 19
print(solution(437674, 3))
print(solution(110011, 10))
