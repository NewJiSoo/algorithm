# https://www.acmicpc.net/problem/14889
# 메모리 : 31120 KB, 시간 : 5416 ms
# 참고 코드 : https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-14889-%ED%95%B4%EC%84%A4-python-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC

import sys
input = sys.stdin.readline

N = int(input())
person = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

mini = 1e9


def backtrack(depth, start):
    global mini
    if depth == N//2:
        team1, team2 = 0, 0  # 팀1, 팀2 능력치의 합
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += person[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += person[i][j]
        mini = min(mini, abs(team1-team2))  # 이전 최소값 vs 현재 최소값
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True  # i번째 선수 포함 시
            backtrack(depth+1, i+1)
            visited[i] = False  # 한차례 팀 나눴으면 다른 경우의 수를 계산하기 위해 원래대로 돌리기


backtrack(0, 0)
print(mini)
