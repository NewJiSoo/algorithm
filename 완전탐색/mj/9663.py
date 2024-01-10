# https://www.acmicpc.net/problem/9663
# 메모리 : 199124 KB, 시간 : 29408 ms  by pypy, python3는 시간 초과

N = int(input())
row = [0]*N
count = 0


def check(x):
    for i in range(x):  # x와 i가 같은 행이라면 or
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            # 같은 행이라면(값이 같음) or 같은 대각선에 위치하면(i가 항상 x보다 작기 때문에 뒤에는 abs를 붙이지 않아도 됨)
            return False  # 퀸 안둘래
    return True  # 그곳에 퀸을 두겠다


def backtrack(depth):
    global count
    if depth == N:
        count += 1
        return
    else:
        for i in range(N):
            row[depth] = i  # row[0] = 0 -> row[0] = 1 -> row[0] = 2... 순서로 탐색
            if check(depth):  # 퀸을 두고
                backtrack(depth+1)  # 다음 줄로(행으로) row[1] -> row[2]...


backtrack(0)
print(count)
