# https://www.acmicpc.net/problem/17503
# 메모리 : 64284 KB, 시간 : 532 ms
# 이분탐색으로 풀지 못해서 힙 이용
# 참고 코드 : https://velog.io/@highway92/%EB%B0%B1%EC%A4%80-17503%EB%B2%88-%EB%A7%A5%EC%A3%BC-%EC%B6%95%EC%A0%9C

import sys
import heapq
input = sys.stdin.readline


def solve():
    n, m, k = map(int, input().split())
    beer = []
    likes = []

    for _ in range(k):
        a, b = map(int, input().split())
        beer.append((a, b))

    # 도수를 기준으로 정렬(낮은것부터 우선순위)
    beer.sort(key=lambda x: x[1])
    # 선호도 합
    hap = 0

    for i in beer:
        # 맥주 고르기
        if len(likes) < n:
            # 선호도를 기준으로 likes에 들어간다(선호도가 가장 낮은 것이 우선)
            heapq.heappush(likes, i)
            hap += i[0]
        # n개 맥주 모두 골랐으면 선호도 비교
        if len(likes) == n:
            # 만약 선호도 기준을 만족하면 최소도수 반환
            # -> 도수가 낮은 것 부터 정렬해서 높은게 나중으로 가는데 최대 도수를 출력할 것이니 i번째를 return 한다.
            if hap >= m:
                return i[1]
            else:
                # 선호도가 낮은 것이 likes에서 pop 된다
                hap -= heapq.heappop(likes)[0]

    # for 문을 전부 돌아도 return 되는 것이 없다면 -1을 반환한다.
    return -1


print(solve())
