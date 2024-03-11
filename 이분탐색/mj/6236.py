# https://www.acmicpc.net/problem/6236
# 메모리 : 31120 KB, 시간 : 44 ms

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))

start = min(arr)
end = sum(arr)  # 최대 지점을 배열들의 합계로 정한다.

while start <= end:
    mid = (start+end)//2
    charge = mid			# 현재 가진 돈. 처음 인출.
    num = 1				    # 인출 횟수
    for i in range(N):		# n일 살기 시작
        if charge < arr[i]:  # 가진 돈이 부족하면 돈 인출
            charge = mid
            num += 1
        charge -= arr[i]

    # M번보다 더 많이 인출하는 경우 -> 금액을 늘려줘서 출금 횟수를 줄인다(start를 높인다)
    # 출금해야 하는 금액의 최대값보다 mid값이 작은경우 -> 금액을 늘려준다
    if num > M or mid < max(arr):
        start = mid + 1

    else:
        end = mid - 1
        ans = mid

print(ans)
