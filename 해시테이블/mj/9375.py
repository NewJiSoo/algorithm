# https://www.acmicpc.net/problem/9375
# 메모리 : 31120 KB, 시간 : 60 ms

test_c = int(input())

for _ in range(test_c):
    n = int(input())
    cloths = {}
    for _ in range(n):
        v, k = input().split()
        if k in cloths:
            cloths[k].append(v)  # 키가 존재하지 않으면 추가
        else:
            cloths[k] = [v]  # 이미 키가 존재하는 경우 리스트 형태로 값을 추가해야 함

    cnt = 1
    for i in cloths:
        cnt *= (len(cloths[i])+1)  # 같은 종류의 옷 수len(cloths[i]) + 착용하지 않는 경우(1)
    print(cnt-1)  # 알몸인 경우 제외
