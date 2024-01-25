# https://www.acmicpc.net/problem/9935
# 메모리 : 42300 KB, 시간 : 756 ms

string = input()
boom = input()
stack = []
boom_len = len(boom)

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-boom_len:]) == boom:
        for _ in range(boom_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
