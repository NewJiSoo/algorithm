# https://www.acmicpc.net/problem/23309
# 메모리 : 208624 KB, 시간 : 1632 ms
# 참고코드 : https://www.acmicpc.net/source/65939710

import sys

N, M = map(int, sys.stdin.readline().split())
Y_list = list(map(int, sys.stdin.readline().split()))

prev_station = [0]*1000001  # 각 역의 이전역과 다음역 저장, 역 고유 번호 1~1000000 이하의 양의 정수
next_station = [0]*1000001


for idx, num in enumerate(Y_list):  # 역 리스트를 인덱스, 역번호로 나눔
    pre_idx = idx - 1
    next_idx = (idx+1) % N  # 현재역 idx의 다음 역을 첫번째역 idx(0)로 설정
    # ex)4개의 역 중 4번째 역(마지막 역)일 때 다음역의 인덱스는 : (3+1) % 4의 나머지 = 0, 마지막 역의 다음역이 첫번째역(인덱스 0번째)가 됨

    # num역의 이전역 찾아서 저장 -> num 위치를 찾으면 이전역 정보를 알 수 있음
    prev_station[num] = Y_list[pre_idx]
    # num역의 다음역 찾아서 저장 -> num 위치를 찾으면 다음역 정보를 알 수 있음
    next_station[num] = Y_list[next_idx]


def insert_after(cur, new):  # A -> B -> C // 현재위치:B, 추가:D
    next_node = next_station[cur]  # 현재 위치 다음역 ex) C
    next_station[cur] = new  # 현재 위치 다음역을 새로운 역으로 바꾸기 ex) B->C에서 B->D로 바꿈
    next_station[new] = next_node  # 새로운 역 다음역을 현재 위치 다음역으로 바꾸기 ex) D->C
    prev_station[new] = cur  # 새로운역 이전역 추가 ex) B->D
    prev_station[next_node] = new  # 바꾼역을 새로운 역과 연결 ex) D->C
    # 결과 : A -> B -> D -> C


def remove(cur):
    prev_node = prev_station[cur]
    next_node = next_station[cur]

    prev_station[next_node] = prev_node
    next_station[prev_node] = next_node


for _ in range(M):
    x = sys.stdin.readline().split()

    if x[0] == 'BN':
        print(next_station[int(x[1])])
        insert_after(int(x[1]), int(x[2]))

    elif x[0] == 'BP':
        print(prev_station[int(x[1])])
        x_pre = prev_station[int(x[1])]
        insert_after(x_pre, int(x[2]))

    elif x[0] == 'CN':
        x_next = next_station[int(x[1])]
        print(x_next)
        remove(x_next)

    elif x[0] == 'CP':
        x_pre = prev_station[int(x[1])]
        print(x_pre)
        remove(x_pre)
