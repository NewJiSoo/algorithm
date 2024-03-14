# https://www.acmicpc.net/problem/16953
# 메모리 : 31120 KB, 시간 : 40 ms

A, B = map(int, input().split())

cnt = 1
while (B != A):
    C = B
    if B % 2 == 0:
        cnt += 1
        B = (B // 2)
    elif B % 10 == 1:
        B //= 10
        cnt += 1

    if B == C:
        print(-1)
        break
if A == B:
    print(cnt)
