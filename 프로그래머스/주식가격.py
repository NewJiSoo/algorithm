
def solution(prices):
    answer = [0] * len(prices)
    dec = []

    for i in range(len(prices)):
        if len(dec) > 0:
            # 가격이 떨어졌으면
            while dec and prices[dec[-1]] > prices[i]:
                last = dec.pop()
                answer[last] = i - last
        dec.append(i)

    for i in dec:
        answer[i] = len(prices) - i - 1

    return answer


print(solution([1, 2, 3, 2, 3]))
