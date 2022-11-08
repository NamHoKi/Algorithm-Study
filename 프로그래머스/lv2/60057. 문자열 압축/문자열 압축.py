def solution(s):
    answer = len(s)
    for i in range(1,len(s)+1):        
        x = s[:i] # 기준이 될 문자열
        temp = ''
        cnt = 1
        for j in range(i,len(s)+i,i):
            y = s[j:j+i] # 비교할 문자열
            if y == x:
                cnt += 1
            else:
                if cnt == 1:
                    temp += x
                    x = y
                else:
                    temp += str(cnt) + x
                    x = y
                    cnt = 1
        if len(temp) < answer and 0 < len(temp):           
            answer = len(temp)
    
    return answer