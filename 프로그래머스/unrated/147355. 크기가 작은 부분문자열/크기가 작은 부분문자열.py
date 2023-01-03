def solution(t, p):
    answer = 0
    l, n = len(p), int(p)
    
    for i in range(len(t) - l + 1) :
        temp_num = int(t[i:i+l])
        if n >= temp_num :
            answer += 1
    
    return answer