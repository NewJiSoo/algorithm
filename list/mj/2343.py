# https://www.acmicpc.net/problem/2343
# 메모리 : 42204 KB, 시간 : 424 ms

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

start, end = max(N_list), sum(N_list)

while start <= end:
    mid = (start+end) // 2
    total = 0  # 한 레코드 강의 길이 합
    count = 1  # 레코드 수

    for i in N_list:
        total += i
        if total > mid:  # 강의 합(total)이 기준 강의 길이(mid)보다 커지면 다음 레코드로 넘어가기
            count += 1  # 레코드 수 += 1
            total = i  # 새 레코드에 현재 강의 길이 더하기(왜냐면 전 레코드에 현재 강의를 넣으면 길이를 초과했으니)

    if count <= M:  # 레코드 수가 기준(M)보다 작으면 강의 합(total)을 더 작게해 레코드 수를 늘린다
        end = mid - 1

    else:
        start = mid + 1

print(start)
