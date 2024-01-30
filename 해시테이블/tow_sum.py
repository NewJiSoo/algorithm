# 전체 시간복잡도 O(n)
def two_sum(nums, target):
    memo = {}

    # 시간복잡도 O(n)
    for v in nums:
        memo[v] = 1

    # 시간복잡도 O(n)
    for v in nums:
        needed_number = target - v
        # 시간복잡도 O(1) - 딕셔너리로 찾을 경우
        if needed_number in memo and needed_number != v:
            # if needed_number in nums:
            # 이렇게 리스트에서 찾으면 시간복잡도 O(n) -> 전체 시간복잡도는 O(n^2)이 됨
            return True
        return False
