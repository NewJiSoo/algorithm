# https://www.acmicpc.net/problem/14501
# 참고 코드 : https://www.youtube.com/watch?v=9GLuPXiIC3s

N = int(input())

T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())


# 백트래킹
# 메모리 : 31120 KB, 시간 : 48 ms
def dfs(day, pay):
    global ans

    # 종료조건 : 가능한 day(종료)에 관련된것으로 정의
    if day >= N:
        ans = max(ans, pay)
        return

    # 상담 조건
    # 상담이 퇴사일 전에 가능한 경우
    # dfs(현재 날짜+일할 때 걸리는 날짜, 현재 금액+일하면 받는 금액)
    if day + T[day] <= N:
        dfs(day+T[day], pay+P[day])

    # 상담하지 않는 경우 -> 다음 날짜로 넘어감, 당연히 돈도 받지 않음
    dfs(day+1, pay)


ans = 0
dfs(0, 0)
print(ans)


# DP
# 메모리 : 31120 KB, 시간 : 40 ms
dp = [0]*(N+1)

# 뒤에서 앞으로(완료기준), 0이 포함되기 때문에 N-1부터 시작함
for day in range(N-1, -1, -1):
    # 기간 내에 상담완료 가능하면
    if day+T[day] <= N:
        dp[day] = max(dp[day+1], dp[day+T[day]]+P[day])
    # 상담하지 않는 경우 이전 수익 그대로
    else:
        dp[day] = dp[day+1]

print(dp[0])
