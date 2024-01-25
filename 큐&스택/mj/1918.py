# https://www.acmicpc.net/problem/1918
# 메모리 : 31120 KB, 시간 : 40 ms
# 참고 코드 : https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python

string = input()
stack = []
ans = ''

for i in string:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()

print(ans)
