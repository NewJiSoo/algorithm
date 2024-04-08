def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(cur_k, cnt):
        if 0 > cnt:
            return cnt - 1

        max_cnt = cnt
        for i in range(len(dungeons)):
            if cur_k >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                max_cnt = max(max_cnt, dfs(cur_k-dungeons[i][1], cnt + 1))
                visited[i] = False

        return max_cnt

    answer = dfs(k, 0)

    return answer


print(solution(80, 	[[80, 20], [50, 40], [30, 10]]))
