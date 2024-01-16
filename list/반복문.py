# 시간복잡도 O(n**2)
def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return True

    return False
