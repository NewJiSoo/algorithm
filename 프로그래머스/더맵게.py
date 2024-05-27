# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        # a를 먼저 pop 하기 때문에 배열에서 한 요소만 남아있을 때 배열의 길이가 0이 된다.
        if len(scoville) == 0:
            return -1

        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
