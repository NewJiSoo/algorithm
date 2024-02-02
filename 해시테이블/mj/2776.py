# https://www.acmicpc.net/problem/2776
# 메모리 : 250468 KB, 시간 : 1640 ms

T = int(input())
for _ in range(T):
    N = int(input())
    N_list = map(int, input().split())

    M = int(input())
    M_list = list(map(int, input().split()))

    soo_dic = {}

    for i in N_list:
        soo_dic[i] = True

    for i in M_list:
        if i in soo_dic:
            print(1)
        else:
            print(0)
