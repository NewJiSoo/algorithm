# https://www.acmicpc.net/problem/4195
# 메모리 : 42900 KB, 시간 : 4228 ms
# union-find 개념 : https://velog.io/@kimdukbae/Union-Find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# 코드 출처 : https://chancoding.tistory.com/50

tc = int(input())


def find(x):
    if x != parent[x]:  # 부모노드가 있는 경우
        parent[x] = find(parent[x])  # 루트노드 찾기
    return parent[x]  # 루트 노드 값 반환


def union(a, b):
    a = find(a)  # a가 포함되어있는 루트
    b = find(b)  # b가 포함되어있는 루트

    if a != b:  # 루트 노드가 다른 경우 b를 a의 루트노드 값으로 바꿔주기
        parent[b] = a
        number[a] += number[b]  # a의 합계에 b 추가
    print(number[a])


for _ in range(tc):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
