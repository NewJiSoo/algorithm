# https://www.acmicpc.net/problem/12015
# 메모리 : 146408 KB, 시간 : 956 ms
# 참고 코드 : https://www.youtube.com/watch?v=voklbG1wU8A
# bisect 사용 방법 : https://gr-st-dev.tistory.com/864

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

long = []

for i in A:
    if not long or long[-1] < i:
        long.append(i)
    else:
        a = bisect_left(long, i)  # O(longN)
        long[a] = i

print(len(long))
