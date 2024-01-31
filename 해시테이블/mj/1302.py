# https://www.acmicpc.net/problem/1302
# 메모리 : 31120 KB, 시간 : 40 ms

N = int(input())

best = {}
for _ in range(N):
    book = input()
    if book in best:
        best[book] += 1
    else:
        best[book] = 1

best_seller = []

max_val = max(best.values())
for k, v in best.items():
    if v == max_val:
        best_seller.append(k)
# best_seller = [k for k, v in best.items() if v==max_val]

best_seller.sort()
print(best_seller[0])
