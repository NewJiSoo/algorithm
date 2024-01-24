# https://www.acmicpc.net/problem/17298
# 메모리 : 248148 KB, 시간 : 540 ms, pypy
# 참고 코드 : https://hongcoding.tistory.com/40

import sys
input = sys.stdin.readline

A = int(input())
A_list = list(map(int, input().split()))
stack = []  # 인덱스 값을 넣을 스택
ans = [-1] * A

stack.append(0)
for i in range(1, A):
    # 스택이 비어있을 때 까지 반복, 인덱스+값이 큰 수 찾기(오큰수)
    while stack and A_list[i] > A_list[stack[-1]]:
        ans[stack.pop()] = A_list[i]  # 스택에 저장된 마지막 인덱스에 값 넣어주기
    stack.append(i)  # i번째 수가 스택에 쌓여있는 인덱스들의 값보다 작다면 다음 인덱스로 넘어감

print(*ans)  # 공백으로 구분해서 출력
