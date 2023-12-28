# https://leetcode.com/problems/min-cost-climbing-stairs/


# 1. 완전 탐색
#   시간 복잡도 O(2**n) => O(2**1000) 너무 큼!
cost = [...]  # cost가 주어졌을 때


def dfs(n):
    if n == 0 and n == 1:  # 오르려는 계단 시작이 0층, 1층 이니까
        return 0

    return min(dfs(n-1)+cost[n-1], dfs(n-2)+cost[n-2])
    #  둘중 최소값(n-1층에서 오기 VS n-2층에서 오기)


# 2. DP(top-down)
#   시간 복잡도 O(n) => O(10**3)
memo = {}


def dp(n):
    if n == 0 and n == 1:
        return 0

    if n not in memo:  # n을 계산한 적이 없으면(적어도 1번은 계산해야 함)
        min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])

    return memo[n]


# 3. DP(bottom-up)
#   시간 복잡도 O(n) => O(10**3)
def dp(n):
    memo = [-1]*n  # 배열 초기화
    memo[0] = 0
    memo[1] = 0  # 시작 지점

    for i in range(2, n+1):  # 2부터 n까지
        memo[n] = min(memo[i-1]+cost[i-1], memo[i-2]+cost[i-2])

    return memo[n]
