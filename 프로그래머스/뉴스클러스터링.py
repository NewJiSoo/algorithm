def make(str):
    multi = {}
    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            pair = str[i:i+2].lower()
            multi[pair] = multi.get(pair, 0) + 1
    return multi


def solution(str1, str2):
    arr1 = make(str1)
    arr2 = make(str2)
    intersection = sum(min(arr1.get(key, 0), arr2.get(key, 0)) for key in arr1)
    union = sum(arr1[i] for i in arr1) + sum(arr2[j]
                                             for j in arr2) - intersection

    if union == 0:
        return 65536
    else:
        return int(intersection / union * 65536)


print(solution("FRANCE", "french"))  # 정답: 16384
