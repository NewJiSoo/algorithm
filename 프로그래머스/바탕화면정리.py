def solution(wallpaper):
    row = len(wallpaper)
    col = len(wallpaper[0])
    min_row = None
    min_col = None
    max_row = None
    max_col = None

    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == "#":
                if min_row is None:
                    min_row = i
                    min_col = j
                    max_row = i+1
                    max_col = j+1
                else:
                    min_row = min(min_row, i)
                    min_col = min(min_col, j)
                    max_row = max(max_row, i+1)
                    max_col = max(max_col, j+1)

    answer = [min_row, min_col, max_row, max_col]
    return answer


print(solution([".#...", "..#..", "...#."]))  # [0, 1, 3, 4]
