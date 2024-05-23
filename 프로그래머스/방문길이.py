def solution(dirs):
    answer = 0
    visited = set()
    x, y = 0, 0

    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for i in dirs:
        nx, ny = x + move[i][0], y + move[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            edge = (x, y, nx, ny) if (x, y) < (nx, ny) else (nx, ny, x, y)

            # 새로운 경로라면 집합에 추가하고, 카운트 증가
            if edge not in visited:
                visited.add(edge)
                answer += 1

            # 현재 위치 업데이트
            x, y = nx, ny

    return answer


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
