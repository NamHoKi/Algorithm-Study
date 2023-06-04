def solution(dots):
    answer = 0
    x1, y1 = min([dots[0][0], dots[1][0], dots[2][0], dots[3][0]]), min([dots[0][1], dots[1][1], dots[2][1], dots[3][1]])
    x2, y2 = max([dots[0][0], dots[1][0], dots[2][0], dots[3][0]]), max([dots[0][1], dots[1][1], dots[2][1], dots[3][1]])
    
    return abs(x2-x1) * abs(y2-y1)