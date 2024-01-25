# https://www.acmicpc.net/problem/2493
# 메모리 : 89736 KB, 시간 : 536 ms

N = int(input())
tower = list(map(int, input().split()))
stack = []
ans = [0]*N


for i in range(N-1, -1, -1):
    while stack and tower[i] > tower[stack[-1]]:
        ans[stack.pop()] = i+1
    stack.append(i)

print(*ans)
