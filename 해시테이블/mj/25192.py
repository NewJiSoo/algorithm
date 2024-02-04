# https://www.acmicpc.net/problem/25192
# 메모리 : 38116 KB, 시간 : 3856 ms

N = int(input())

dic = {}
cnt = 0

for _ in range(N):
    id = input()
    if id == "ENTER":
        dic = {}
    else:
        if not id in dic:
            dic[id] = True
            cnt += 1
        else:
            continue
print(cnt)
