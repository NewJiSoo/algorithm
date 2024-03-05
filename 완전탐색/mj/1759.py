# https://www.acmicpc.net/problem/1759
# 메모리 : 31120 KB, 시간 : 48 ms

L, C = map(int, input().split())
alp = list(map(str, input().split()))
mo = ["a", "e", "i", "o", "u"]

alp.sort()


def check(curr):
    m_cnt = 0
    j_cnt = 0

    for i in curr:
        if i in mo:
            m_cnt += 1
        else:
            j_cnt += 1
    if m_cnt >= 1 and j_cnt >= 2:
        return True
    else:
        return False


def back(start, curr):
    if len(curr) == L:
        if check(curr):
            print("".join(curr))
            return

    for i in range(start, C):
        curr.append(alp[i])
        back(i+1, curr)
        curr.pop()


back(0, [])
