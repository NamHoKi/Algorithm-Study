def solution(dirs):
    answer = 0
    visited = [[False] * 11 for _ in range(11)]
    offsets = {'U':[0, 1, 'D'], 'L':[-1, 0, 'R'], 'R':[1, 0, 'L'], 'D':[0, -1, 'U']}
    
    x, y = 5, 5
    for D in dirs :
        dx, dy, RD = offsets[D]
        if not ((0 <= x + dx <= 10) and (0 <= y + dy <= 10)) :    # 맵 밖으로 가지 않으면, -> 맵 밖으로 가면 무시
            continue

        if visited[x][y] == False :     # 처음 간 좌표라면,
            visited[x][y] = [D]         # 현재 가는 길 체크
            answer += 1
            x, y = x + dx, y + dy
            if visited[x][y] == False :     # 처음 간 좌표라면,
                visited[x][y] = [RD]
            else :                          # 처음 간 좌표가 아니라면,
                if not (RD in visited[x][y]) :
                    visited[x][y].append(RD)
        else :
            if not (D in visited[x][y]) :   # 처음 가본 길이라면,
                visited[x][y].append(D)     # 현재 가는 길 체크
                answer += 1
            x, y = x + dx, y + dy
            if visited[x][y] == False :     # 처음 간 좌표라면,
                visited[x][y] = [RD]
            else :                          # 처음 간 좌표가 아니라면,
                if not (RD in visited[x][y]) :
                    visited[x][y].append(RD)
                
    return answer