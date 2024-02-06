# https://www.acmicpc.net/problem/9934
# 메모리 : 31120 KB, 시간 : 40 ms

K = int(input())
tree = list(map(int, input().split()))

ans = [[] for _ in range(K)]


def dfs(tree, depth):
    mid = (len(tree) // 2)

    ans[depth].append(tree[mid])

    if len(tree) == 1:
        return

    dfs(tree[:mid], depth+1)
    dfs(tree[mid+1:], depth+1)


dfs(tree, 0)

for i in ans:
    print(*i)
