def solution(s):
    answer = [0, 0]
    while True :
        if s == '1' :
            return answer
        l = len(s)
        s = s.replace('0', '')
        answer[0] += 1
        answer[1] += l - len(s)
        
        s = bin(len(s))[2:]
    
    return answer