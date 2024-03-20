def solution(cards1, cards2, goal):
    answer = 'Yes'
    ca1 = 0
    ca2 = 0
    for i in goal:
        if ca1 >= len(cards1) and ca2 >= len(cards2):  # 두 카드 리스트 모두 모두 소진한 경우
            answer = 'No'
            break
        if ca1 < len(cards1) and i == cards1[ca1]:  # cards1에 속하는 경우
            ca1 += 1
        elif ca2 < len(cards2) and i == cards2[ca2]:  # cards2에 속하는 경우
            ca2 += 1
        else:  # 어느 카드 리스트에도 속하지 않는 경우
            answer = 'No'
            break

    return answer


print(solution(["i", "drink", "water"], ["want", "to"],
      ["i", "want", "to", "drink", "water"]))  # 정답:Yes
print(solution(["i", "water", "drink"], ["want", "to"],
      ["i", "want", "to", "drink", "water"]))  # 정답:No
