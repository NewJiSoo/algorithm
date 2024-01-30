def longestConsecutive(nums):
    longest = 0
    num_dict = {}

    # 시간복잡도 O(n)
    for num in nums:
        num_dict[num] = True
    # 컴프리핸션 방법 num_dict = {x:True for x in nums}

    # 딕셔너리 대신 해시셋을 사용해도 됨
    # num_set = set(nums)

    # 시간복잡도 O(n)
    for num in num_dict:
        if num - 1 not in num_dict:  # 시간복잡도 O(1)
            cnt = 1
            target = num + 1
            while target in num_dict:  # 시간복잡도 O(1)
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


longestConsecutive([6, 7, 100, 5, 4, 4])
