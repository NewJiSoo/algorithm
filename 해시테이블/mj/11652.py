# https://www.acmicpc.net/problem/11652
# 메모리 : 42900 KB, 시간 : 4228 ms

N = int(input())

dec = {}
for _ in range(N):
    card = int(input())
    if card in dec:
        dec[card] += 1
    else:
        dec[card] = 1

max_val = max(dec.values())
min_dec = [k for k, v in dec.items() if max_val == v]
print(min(min_dec))
