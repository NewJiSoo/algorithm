# https://www.acmicpc.net/problem/14425
# 메모리 : 36372 KB, 시간 : 920 ms

N, M = map(int, input().split())

N_dic = {}
for _ in range(N):
    x = input()
    N_dic[x] = 1

cnt = 0
for _ in range(M):
    y = input()

    if y in N_dic:
        cnt += 1

print(cnt)
