def solution(board, h, w):
    answer = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    row = len(board)
    col = len(board[0])

    for i in range(4):
        if 0 <= h+dh[i] < row and 0 <= w+dw[i] < col:
            if board[h][w] == board[h+dh[i]][w+dw[i]]:
                answer += 1

    return answer


print(
    solution(
        [["blue", "red", "orange", "red"],
         ["red", "red", "blue", "orange"],
         ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]], 1, 1))
