# https://www.acmicpc.net/problem/14888
# 메모리 : 31120 KB, 시간 : 64 ms

# 참고 코드 : https://ryngryng.tistory.com/32

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = -1e9
mini = 1e9


def dfs(depth, total, plus, minus, multi, divide):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)  # 최대값
        mini = min(total, mini)  # 최소값
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus, minus, multi, divide-1)
        # total//num[depth] 사용 시 음수의 나눗셈에서 문제 제시 조건대로 몫을 내지 않음


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)
