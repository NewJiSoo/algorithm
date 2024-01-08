# nums = [1, 2, 3, 4]로 만들 수 있는 모든 조합을 반환하시오

def Solution(nums, k):
    result = []

    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()

    backtrack(start=0, curr=[])
    return result


print(Solution(nums=[1, 2, 3, 4], k=2))
