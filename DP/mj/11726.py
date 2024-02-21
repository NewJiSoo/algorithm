# https://www.acmicpc.net/problem/11726
# 메모리 : 108080 KB, 시간 : 112 ms, pypy

import sys
input = sys.stdin.readline

n = int(input())

memo = [0] * 1001
memo[1] = 1
memo[2] = 2
for i in range(3, n+1):
    memo[i] = (memo[i-1]+memo[i-2]) % 10007

print(memo[n])
