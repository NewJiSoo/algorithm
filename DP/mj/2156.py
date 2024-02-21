# https://www.acmicpc.net/problem/2156
# 메모리 : 31120 KB, 시간 : 48 ms

import sys
input = sys.stdin.readline

n = int(input())

podo = [0] * 10001
for i in range(1, n+1):
    podo[i] = int(input())

memo = [0] * 10001
memo[1] = podo[1]
memo[2] = podo[2]+podo[1]

for i in range(3, n+1):
    memo[i] = max(memo[i-2]+podo[i], memo[i-1],
                  memo[i-3]+podo[i-1]+podo[i])
print(memo[n])
