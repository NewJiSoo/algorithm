# https://www.acmicpc.net/problem/4358
# 메모리 : 31120 KB, 시간 : 500 ms

import sys
input = sys.stdin.readline

world_list = {}
cnt = 0

while True:
    world = input().strip()
    if not world:
        break

    cnt += 1
    if world in world_list:
        world_list[world] += 1
    else:
        world_list[world] = 1


sort_list = sorted(world_list.items())

for k, v in sort_list:
    per = (v/cnt*100)

    # 최신 포메팅 방식
    print("{} {:.4f}" .format(k, per))
    # print(f"{k} {per:.4f}")

    # 옛날 포매팅 방식
    # print("%s %.4f" % (k, per))
