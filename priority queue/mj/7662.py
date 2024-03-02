# https://www.acmicpc.net/problem/7662
# 메모리 : 288376 KB, 시간 : 8736 ms
# 참고 코드 : https://chaewsscode.tistory.com/138

import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    max_dec = []
    min_dec = []
    visited = [False] * k

    for i in range(k):
        cmd, n = list(map(str, input().split()))
        n = int(n)

        if cmd == 'I':
            heapq.heappush(max_dec, (-n, i))
            heapq.heappush(min_dec, (n, i))
            visited[i] = True
        elif n == 1:
            # max_dec이 존재하고 i에 해당하는 숫자가 False일때 max_dec에서 pop
            # 만약 i가 False라면 그 숫자는 버려진 숫자 -> min 혹은 max에서 버려진 숫자라 사용X
            while max_dec and not visited[max_dec[0][1]]:
                heapq.heappop(max_dec)
            if max_dec:
                visited[max_dec[0][1]] = False
                heapq.heappop(max_dec)
        else:
            while min_dec and not visited[min_dec[0][1]]:
                heapq.heappop(min_dec)
            if min_dec:
                visited[min_dec[0][1]] = False
                heapq.heappop(min_dec)

    # 버려진 숫자들 제거 -> visited에 True인 숫자들만 고르는 과정
    while min_dec and visited[min_dec[0][1]] == False:
        heapq.heappop(min_dec)
    while max_dec and visited[max_dec[0][1]] == False:
        heapq.heappop(max_dec)

    if max_dec and min_dec:
        print(-max_dec[0][0], min_dec[0][0])
    else:
        print('EMPTY')
