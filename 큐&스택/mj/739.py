# https://leetcode.com/problems/daily-temperatures/description/

def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []

    for day, temp in enumerate(temperatures):

        while stack and stack[-1][1] < temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = day - prev_day

        stack.append((day, temp))
    return ans
