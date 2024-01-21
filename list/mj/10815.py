# https://www.acmicpc.net/problem/10815
# 메모리 : 97304 KB, 시간 : 3356 ms

import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())


for i in M_list:
    start, end = 0, N-1
    exist = False

    while start <= end:
        mid = (start+end)//2
        if N_list[mid] > i:
            end = mid - 1
        elif N_list[mid] < i:
            start = mid + 1
        else:
            exist = True
            break

    print(1 if exist else 0, end=' ')
