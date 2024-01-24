# https://www.acmicpc.net/problem/10799
# 메모리 : 31552 KB, 시간 : 60 ms

gh = input()
count = 0
stack = []

for i in range(len(gh)):
    if gh[i] == '(':

        stack.append('(')
    else:
        if gh[i-1] == '(':
            stack.pop()
            count += len(stack)

        else:
            stack.pop()
            count += 1

print(count)
