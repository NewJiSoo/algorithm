def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                return 1
            else:
                return 0

        else:
            return dfs(idx+1, total + numbers[idx]) + dfs(idx+1, total - numbers[idx])
    answer = dfs(0, 0)
    return answer
