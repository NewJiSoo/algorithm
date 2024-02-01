# https://www.acmicpc.net/problem/12015
# 시간초과

N = int(input())
A = list(map(int, input().split()))

# 각 인덱스에서 끝나는 가장 긴 증가하는 부분 수열의 길이를 저장할 배열 초기화
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 현재 요소가 이전 요소보다 큰지 확인
        if A[i] > A[j]:
            # 현재 인덱스에서 끝나는 가장 긴 증가하는 부분 수열의 길이 업데이트
            dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)

print(result)
