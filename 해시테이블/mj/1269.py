# https://www.acmicpc.net/problem/1269
# 메모리 : 81352 KB, 시간 : 256 ms

n, m = input().split()

A = set(map(int, input().split()))
B = set(map(int, input().split()))


print(len(A-B)+len(B-A))
