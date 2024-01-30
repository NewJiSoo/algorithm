# https://www.acmicpc.net/problem/11478
# 메모리 : 240712 KB, 시간 : 516 ms

S = input()
total = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        total.add(S[i:j+1])
print(len(total))
