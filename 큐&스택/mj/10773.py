# https://www.acmicpc.net/problem/10773
# 메모리 : 31900 KB, 시간 : 80 ms

import sys
input = sys.stdin.readline

K = int(input())

stack = []
for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))
