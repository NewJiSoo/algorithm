# https://www.acmicpc.net/problem/15686
# 메모리 : 31120 KB, 시간 : 416 ms
# 도움 : chatGPT

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])


def chicken_distance(selec_chichen):
    total = 0
    for i in range(N):
        for j in range(len(city[i])):
            if city[i][j] == 1:
                result = [abs(i-x)+abs(j-y) for x, y in selec_chichen]
                total += min(result)
    return total


mini = float('inf')


def backtrack(selec_chichen, start):
    global mini
    if len(selec_chichen) == M:
        mini = min(mini, chicken_distance(selec_chichen))
        return

    for i in range(start, len(chicken)):
        selec_chichen.append(chicken[i])
        backtrack(selec_chichen, i+1)
        selec_chichen.pop()


backtrack([], 0)
print(mini)
