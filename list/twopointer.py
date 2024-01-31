# 정렬 시간 복잡도 nlog(n)

def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1

    while l < r:
        if nums[l]+nums[r] > target:
            r -= 1
        elif nums[l]+nums[r] < target:
            l += 1
        elif nums[l]+nums[r] == target:
            return True

    return False