def solution(n):
    answer = 0

    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(i**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer
