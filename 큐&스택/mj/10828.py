# https://www.acmicpc.net/problem/10828
# 메모리 : 31120 KB, 시간 : 52 ms

import sys
input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    cdm = list(map(str, input().split()))

    if cdm[0] == 'push':
        stack.append(cdm[1])

    elif cdm[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif cdm[0] == 'size':
        print(len(stack))

    elif cdm[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cdm[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
