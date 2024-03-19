# 1. 시간 초과
# def solution(players, callings):
#     for calling in callings:
#         idx = players.index(calling)
#         if idx > 0:  # 해당 선수가 이미 1등이 아닌 경우에만 추월 처리
#             players[idx], players[idx-1] = players[idx-1], players[idx]

#     return players


# 2. 시간 초과 (정렬때문인 것 같다)
# def solution(players, callings):
#     ranking = {name: idx+1 for idx, name in enumerate(players)}

#     for i in callings:
#         for name, r in ranking.items():
#             if r == ranking[i]-1:
#                 ranking[name] += 1
#         ranking[i] -= 1

#     ans = sorted(ranking, key=lambda x: ranking[x])

#     return ans

# 3. 성공!
def solution(players, callings):
    ranking = {name: idx for idx, name in enumerate(players)}
    for name in callings:
        a = ranking[name]
        ranking[name] -= 1
        ranking[players[a-1]] += 1
        players[a-1], players[a] = players[a], players[a-1]

    return players
