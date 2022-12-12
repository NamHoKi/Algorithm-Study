def solution(s):
    answer = 0
    x = -1
    x_cnt = 0
    not_x_cnt = 0
    
    for i in range(len(s)):
        if x == -1:
            x = s[i]
            x_cnt += 1
        else:
        
            if x == s[i]:
                x_cnt += 1
            else:
                not_x_cnt += 1

            if x_cnt == not_x_cnt:
                answer += 1
                x = -1            
                continue

        if i == len(s) - 1 :
            answer += 1        
        
    return answer