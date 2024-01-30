# https://www.acmicpc.net/problem/7785
# 메모리 : 42380 KB, 시간 : 4088 ms

n = int(input())

enter = {}

for _ in range(n):
    name, act = input().split()
    if act == 'enter':
        enter[name] = True
    else:
        del enter[name]

print('\n'.join(sorted(enter.keys(), reverse=True)))
