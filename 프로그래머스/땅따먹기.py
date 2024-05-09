def solution(land):
    answer = 0

    # def back(start, curr, prev):
    #     if len(curr) == len(land):
    #         return sum(curr)

    #     total = 0
    #     for i in range(len(land[0])):
    #         if i != prev:
    #             curr.append(land[start][i])
    #             total = max(back(start+1, curr, i), total)
    #             curr.pop()
    #     return total

    # answer = back(0, [], -1)

    dp = [[0] * len(land[0]) for _ in range(len(land))]
    dp[0] = land[0]

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 이전 행 중 최대값(최대 값의 열) -> 이중 현재 열은 제외
            # j열 이전과 이후 열의 합 배열 중 가장 큰 수 추출
            dp[i][j] = land[i][j] + max(dp[i-1][:j]+dp[i-1][j+1:])

    # 마지막 행의 최대값이 최종 결과
    answer = max(dp[-1])

    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
