# 리스트 [4, 9, 7, 5, 1]에서 두 개의 숫자를 더해 12를 만드시오(중복X)

# 1. 반복문
def Solution(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i, j]


# 2. 재귀
def Solution2(nums, target):
    def backtrack(start, curr):
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr

        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtrack(i+1, curr)

            if ret:  # 중복 계산 피하기, 최초로 찾은 해 반환
                return ret

            curr.pop()
        return None
    return backtrack(0, [])


print(Solution2(nums=[4, 9, 7, 5, 1], target=12))
