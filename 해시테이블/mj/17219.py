# https://www.acmicpc.net/problem/17219
# 메모리 : 49040 KB, 시간 : 12848 ms

N, M = map(int, input().split())

site = {}
for _ in range(N):
    s, p = map(str, input().split())
    site[s] = p

for _ in range(M):
    q = input()
    print(site[q])
