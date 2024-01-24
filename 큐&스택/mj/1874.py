# https://www.acmicpc.net/problem/1874
# 메모리 : 118824 KB, 시간 : 220 ms, pypy

count = 1
temp = True
stack = []
op = []

N = int(input())
for _ in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break


if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
