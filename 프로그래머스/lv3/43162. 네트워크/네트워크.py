def solution(n, computers):
    visited = [False for i in range(n)]
    answer , q = 0, []
        
    for i in range(n) :                 # 모든 node를 방문했는지 체크
        start_node = computers[i][:]
        
        if visited[i] == False :
            visited[i] = True           # 첫 스타팅 포인트로 방문은 answer += 1
            answer += 1
        
        for j in range(n) :             # 현재 노드에서 방문할 수 있는 노드 q에 추가, FIFO
            if start_node[j] == 1 :
                q.append(j)
        
        while q != [] :
            if len(set(visited)) == 1 : # 모든 노드를 방문 했다면
                return answer           # 종료
            f = q.pop(0)                # FIFO
            if visited[f] :             # 이미 방문한 곳이라면
                continue                # 무시
            else :                      # 처음 방문하는 곳이라면
                visited[f] = True               # 방문 체크
                for j in range(n) :             # 이어서 방문할 수 있는 곳 추가
                    if computers[f][j] == 1 :
                        q.append(j)
        
    return answer