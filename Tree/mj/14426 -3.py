# https://www.acmicpc.net/problem/14426
# 메모리 : 41236 KB, 시간 : 1776 ms
# set을 이용한 방법

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
set = set()

for i in range(n):  # 시간복잡도 O(500*n) -> O(n)
    word = input().rstrip()
    for j in range(1, len(word)+1):
        set.add(word[0:j])  # set에 철자마다 슬라이스 해서 넣기, 시간복잡도 O(1)

for i in range(m):
    target = input().rstrip()
    if target in set:  # 이때 시간 복잡도 O(1)
        answer += 1

print(answer)
