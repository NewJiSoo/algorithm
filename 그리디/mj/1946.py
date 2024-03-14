# https://www.acmicpc.net/problem/1946
# 메모리 : 72128 KB, 시간 : 5636 ms
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rank = sorted(arr)
    cnt = 1
    top = 0
    for i in range(1, N):
        if rank[i][1] < rank[top][1]:
            # 바로 이전사람과 비교하는게 아니라 이전 사람 중 등수가 가장 높은 사람과 비교
            top = i
            cnt += 1
    print(cnt)
