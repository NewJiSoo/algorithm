# https://www.acmicpc.net/problem/1072
# 메모리 : 31120 KB, 시간 : 44 ms

X, Y = map(int, input().split())
Z = (Y*100)//X

start = 0
end = X
ans = X

if Z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2

        if ((Y+mid)*100)//(X+mid) > Z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    print(ans)
