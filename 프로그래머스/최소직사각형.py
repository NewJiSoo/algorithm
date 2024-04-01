def solution(sizes):
    w_max, h_max = 0, 0
    for w, h in sizes:
        if w > h:
            w, h = h, w
        if w_max < w:
            w_max = w
        if h_max < h:
            h_max = h
    return w_max * h_max


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
