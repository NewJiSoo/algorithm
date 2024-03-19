def solution(bandage, health, attacks):
    sec, heal, bonus = bandage[0], bandage[1], bandage[2]

    # 힐 시작 시간
    start = 1
    hp = health

    for time, attack in attacks:
        hp += ((time - start) // sec) * bonus + (time - start) * heal
        start = time + 1

        # health를 초과하지 않도록 설정
        if hp >= health:
            hp = health

        hp -= attack

        if hp <= 0:
            return -1

    return hp


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
