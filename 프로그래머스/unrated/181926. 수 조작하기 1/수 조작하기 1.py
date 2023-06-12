def solution(n, control):
    d = {'w':1,'s':-1,'d':10,'a':-10}
    
    for c in control :
        n += d[c]
    return n