def solution(number, limit, power):
    ans = 0
    for i in range(1, number+1):
        cnt = 0
        for k in range(1, int(i ** 0.5)+1):
            # 제곱근 까지만 구하면 시간 초과가 나지 않는다.
            if i % k == 0:
                cnt += 1
                if i // k != k:
                    cnt += 1
        if cnt <= limit:
            ans += cnt
        else:
            ans += power

    return ans


print(solution(10, 3, 2))
