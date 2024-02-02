# https://www.acmicpc.net/problem/20920
# 메모리 : 58960 KB, 시간 : 328 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    alp = input().rstrip()

    if len(alp) < M:
        continue
    else:
        if alp in dic:
            dic[alp] += 1
        else:
            dic[alp] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))


for i in dic:
    print(i[0])
