def solution(tickets):
    answer = []
    def dfs(start,ticList,path):
        path.append(start)
        if len(ticList)==1:
            path.append(ticList[0][1])
            answer.append(path)
            return
        for t in ticList:
            if t[0]==start:
                ticList_copy = ticList.copy()
                ticList_copy.remove(t)
                dfs(t[1],ticList_copy,path.copy())
    dfs("ICN",tickets,[])
    return min(answer)