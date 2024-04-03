from collections import Counter


def solution(participant, completion):
    answer = ''

    ar1 = Counter(participant)
    ar2 = Counter(completion)
    dif = ar1-ar2
    answer = list(dif.keys())[0]

    return answer
