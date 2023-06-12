def solution(s):
    x = s.split(' ')
    a = []
    for n in x :
        a.append(int(n))
    
    return str(min(a)) + ' ' + str(max(a))