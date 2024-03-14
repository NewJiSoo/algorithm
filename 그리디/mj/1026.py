# https://www.acmicpc.net/problem/1026
# 메모리 : 31120 KB, 시간 : 44 ms

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
ans = 0

for i in range(N):
    ans += (A[i]*B[i])

print(ans)
