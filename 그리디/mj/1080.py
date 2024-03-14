# https://www.acmicpc.net/problem/1080
# 메모리 : 31120 KB, 시간 : 48 ms
# 참고코드 : https://puleugo.tistory.com/39

N, M = map(int, input().split())

A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0


cnt = 0
if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    # 끝에서 두개는 뒤집기X -> 3x3으로 뒤집을 것이기 때문에
    for q in range(N-2):
        for w in range(M-2):
            if A[q][w] != B[q][w]:
                cnt += 1
                check(q, w)

if A != B:
    print(-1)
else:
    print(cnt)
