def solution(s):
    answer = ''
    s = s.lower()
    s = s.split(' ')
    print(s)
    for ss in s :
        if len(ss) > 0 and ss[0].islower() :
            answer += chr(ord(ss[0]) - 32) + ss[1:]
        else :
            answer += ss
        answer += ' '
    
    return answer[:-1]