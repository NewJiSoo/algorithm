# https://www.acmicpc.net/problem/19638
# 메모리 : 106008 KB, 시간 : 1760 ms
# 참고 코드 : https://bio-info.tistory.com/195

import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())

gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

gems.sort()  # 무게 오름차순, 무게 같으면 가격 오름차순
bags.sort()  # 가방 무게 오름차순

result = 0  # 결과 출력값 초기화
tmp = []  # 보석의 가격 저장 리스트

for bag in bags:  # 각 가방 무게에 대해
    while gems and gems[0][0] <= bag:  # 가방에 들어가는 보석들을 찾기
        heapq.heappush(tmp, -gems[0][1])  # 가격들을 최대힙에 저장(음수로 저장하여 최소힙을 최대힙으로)
        heapq.heappop(gems)  # 가격 저장한 보석은 버리기
    if tmp:  # bag 무게 이하 보석 가격 다 저장했으면
        result -= heapq.heappop(tmp)  # 제일 가치가 높은 가격 더하기(음수니까 빼기)
print(result)

# gems[0][0]를 여러개 tmp에 저장해도 되는 이유는 가방 무게가 작은 순서로 찾고
# 그 중 가장 비싼 보석 '하나만' 결과에 저장할 것이기 때문!
# ex) gems = [[1, 65], [5, 23], [2, 99]]  bag = [2, 10]
# bag = 2일 때 tmp = [-99, -65], gems=[[5, 23]] -> result -= (-99) = 99
# bag = 10일 때 tmp = [-65, -23], gems = [] -> result -= (-65) = (99+65)
