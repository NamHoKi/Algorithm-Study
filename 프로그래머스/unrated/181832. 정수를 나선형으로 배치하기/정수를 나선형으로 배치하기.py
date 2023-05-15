def solution(n):
    answer = [[0]*n for i in range(n)]
    answer[0][0] = 1
    offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, i = 0, 0, 2
    while i < n*n + 1 :
        x += offsets[0][0]
        y += offsets[0][1]
        
        if 0 <= x < n and 0 <= y < n and answer[x][y] == 0 :    # 처음 온 곳이라면,
                answer[x][y] = i
                i += 1
        else :                                                  # offsets 순환큐
            x -= offsets[0][0]
            y -= offsets[0][1]
            o = offsets.pop(0)
            offsets.append(o)

    return answer