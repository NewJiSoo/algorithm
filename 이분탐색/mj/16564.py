# https://www.acmicpc.net/problem/16564
# 메모리 : 34972 KB, 시간 : 4640 ms

N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]

start = min(X)
end = max(X)+K

# 목표레벨 : mid(mid값 중 최대)
while start <= end:
    mid = (start+end)//2
    cnt = 0  # 임시로 설정한 나눌 수 있는 레벨

    for level in X:
        # 목표 레벨이 현재 캐릭터 레벨보다 크다면 임시레벨을 쓴 것이라고 생각
        if mid > level:
            cnt += (mid-level)

    # 나눌 수 있는 레벨이 K보다 크다면 목표 레벨줄이기(K보다 크게 나눌 수 없기 때문에)
    if cnt > K:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)
