def solution(answers):
    answer = []
    arr = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0, 0, 0]
    
    for target in answers :
        for i in range(3) :
            n = arr[i].pop(0)
            arr[i].append(n)
            if target == n :
                score[i] += 1
    
    for i in range(3) :
        if max(score) == score[i] :
            answer.append(i + 1)
    
    return answer