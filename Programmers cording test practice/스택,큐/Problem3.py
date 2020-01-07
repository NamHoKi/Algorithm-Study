def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        complt = []
        pop_list = []
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                complt.append(i)
        if len(complt) != 0 and complt[0] == 0:
            start = -1
            for i in range(len(complt)):
                if start + 1 == complt[i]:
                    start += 1
                    pop_list.append(i)
                else:
                    break
            for i in range(len(pop_list)-1,-1,-1):
                progresses.pop(i)
                speeds.pop(i)
                cnt += 1
            answer.append(cnt)
    return answer
