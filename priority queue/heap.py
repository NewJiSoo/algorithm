import heapq

foo = [5, 3, 9, 4, 1, 2, 6]

# min heap
heapq.heapify(foo)  # 정렬 O(N) -> 이때 리스트 전체가 정렬되는게 아닌 최소값만 제일 앞에 오게되는 것
heapq.heappop(foo)  # dequeue O(logN)
heapq.heappush(foo, 1)  # enqueue O(logN)

# max heap - 1(heap push가 없음)
heapq._heapify_max(foo)
value = heapq._heappop_max(foo)  # dequeue O(logN)

# max heap - 2
foo = [i * -1 for i in foo]  # -1을 곱해주기
heapq.heapify(foo)
weight = heapq.heappop(foo)
value = -1 * weight  # 원래대로 돌리기(-1 다시 곱해주기)

# max heap - 3
foo = [(i * -1, i) for i in foo]  # -1을 곱해주기 + 원래 값 저장
# foo = [(-5, 5), (-3, 3), (-9, 9)...] 이런 형태로 저장됨
heapq.heapify(foo)
weight, value = heapq.heappop(foo)  # -1을 다시 곱해주지 않아도 value를 구할 수 있음
