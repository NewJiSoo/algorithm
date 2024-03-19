
def solution(park, routes):
    answer = []
    direction = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    cur = []
    row = len(park)
    col = len(park[0])

    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                cur = [i, j]

    for command in routes:
        direct, length = command.split(" ")

        dx, dy = direction[direct]

        next_x = cur[0]
        next_y = cur[1]

        for i in range(int(length)):
            next_x, next_y = next_x + dx, next_y + dy

            if 0 <= next_x < row and 0 <= next_y < col:
                if park[next_x][next_y] == "X":
                    break

        if 0 <= next_x < row and 0 <= next_y < col:
            if park[next_x][next_y] != "X":
                cur = [next_x, next_y]

    answer = cur

    return answer


# Test cases
print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))  # [2, 1]
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))  # [0, 1]
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))  # [0, 0]
