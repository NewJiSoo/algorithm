from collections import Counter


def solution(participant, completion):
    answer = ''

    ar1 = Counter(participant)
    ar2 = Counter(completion)
    dif = ar1-ar2
    answer = list(dif.keys())[0]

    return answer


# 첫 번째 Counter 객체 생성
counter1 = Counter({'a': 3, 'b': 2, 'c': 1})

# 두 번째 Counter 객체 생성
counter2 = Counter({'a': 1, 'b': 2, 'd': 1})

# Counter 객체끼리 더하기(+)
result_add = counter1 + counter2
print("더하기 결과:", result_add)  # 출력: Counter({'a': 4, 'b': 4, 'c': 1, 'd': 1})

# Counter 객체끼리 빼기(-)
result_subtract = counter1 - counter2
print("빼기 결과:", result_subtract)  # 출력: Counter({'a': 2})
