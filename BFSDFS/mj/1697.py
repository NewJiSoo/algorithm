# https://www.acmicpc.net/problem/1697

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)
# 동생은 점 K(0 ≤ K ≤ 100,000)
# 수빈이의 위치가 X일 때
# 걷는다면 1초 후에 X-1 또는 X+1
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램


from collections import deque

N, K = map(int, input().split())
max = 100001
grid = [0] * max
count = 0


def bfs():
    queue = deque()
    queue.append(K, count)

    while queue:
        x, count = queue.popleft()
        if N == K:
            return count
        for i in (x-1, x+1, x*2):
            if 0 <= i < max and grid[i] == 0:
                next = x + i
                grid[next] = grid[i]

                queue.append((next, count + 1))
    return count


print(bfs())
