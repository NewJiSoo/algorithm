# https://leetcode.com/problems/valid-parentheses/description/
# 괄호 유효성 문제
# 1. 짝수, 2. 여는게 먼저, 3. 소.중.대괄호 순서

def isValid(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(")")
        elif p == '{':
            stack.append('}')
        elif p == '[':
            stack.append(']')
        elif not stack or stack.pop() != p:
            return False
    return not stack
