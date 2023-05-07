def solution(s, skip, index):
    answer = ''
        
    for c in s :
        i = index
        while i > 0 :
            if c == 'z' :
                c = 'a'
            else :
                c = chr(ord(c) + 1)
            
            if c in skip :
                continue
            else :
                i -= 1
        answer += c
    
    return answer