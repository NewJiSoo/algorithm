# https://www.acmicpc.net/problem/15900
# 메모리 : 650904 KB, 시간 : 1344 ms
import sys
input = sys.stdin.readline
# 재귀 깊이를 설정하는게 제일 문제인데 10**6으로 설정하니 런타임 에러가 났다
# N의 범위가 2~500,000 이기 때문에 그의 절반정도로 설정하니 통과가 되긴 했는데
# 범위를 설정하는게 아닌 코드를 변경해야 할 것 같다
sys.setrecursionlimit(200000)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (N+1)

# 해당 노드에 대한 깊이를 저장


def dfs(node, depth):
    ans[node] = depth
    for i in graph[node]:
        if ans[i] == 0:
            dfs(i, depth+1)


dfs(1, 0)
total = 0

# 리프노드의 깊이만 더하기
for i in range(2, N+1):
    if len(graph[i]) == 1:
        total += ans[i]

# 짝수 -> No(진다), 홀수->Yes(이긴다)
if total % 2 == 0:
    print("No")
else:
    print("Yes")
