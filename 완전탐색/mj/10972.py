# https://www.acmicpc.net/problem/10972
# 메모리 : 32140 KB, 시간 : 44 ms
n = int(input())

arr = list(map(int, input().split()))

ans = -1
res = []
for i in range(n-2, -1, -1):
    if arr[i+1] > arr[i]:
        sub = 0
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                sub = j
        arr[i], arr[sub] = arr[sub], arr[i]
        res += arr[:i+1]  # res에 0부터 i까지 추가
        res += arr[i+1:][::-1]  # i+1부터 끝까지 역순으로 추가

        print(" ".join(map(str, res)))
        break

else:
    print(-1)
