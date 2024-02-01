# https://www.acmicpc.net/problem/12015
# 메모리 : 144340 KB, 시간 : 3964 ms
# 참고 코드 : https://suri78.tistory.com/199

N = int(input())
A = list(map(int, input().split()))

long = []

for i in A:
    if not long or long[-1] < i:
        long.append(i)
    else:
        left = 0
        right = len(long)
        while left < right:
            mid = (right + left)//2
            if long[mid] < i:
                left = mid+1
            else:
                right = mid
        long[right] = i

print(len(long))
