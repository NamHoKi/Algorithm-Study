def solution(dots):
    a = [[0,1,2,3], [0,2,1,3], [0,3,1,2]]
    
    for d1, d2, d3, d4 in a :
        if (dots[d2][1] - dots[d1][1]) / (dots[d2][0] - dots[d1][0]) == (dots[d4][1] - dots[d3][1]) / (dots[d4][0] - dots[d3][0]) :
            return 1
    return 0