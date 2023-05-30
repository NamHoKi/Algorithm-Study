def solution(polynomial):
    p = polynomial.split(' ')
    x, y = 0, 0
    for a in p :
        if a == '+' :
            continue
            
        if a[-1] == 'x' :
            if len(a) == 1 :
                x += 1
            else :
                x += int(a[:-1])
        else :
            y += int(a)
    
    answer = str(x) + 'x' + ' + ' + str(y)
    if x == 1 :
        answer = answer[1:]
    if x == 0 :
        answer = str(y)
    elif y == 0 :
        answer = str(x) + 'x'
        if x == 1 :
            answer = answer[1:]
    elif x == 0 and y == 0 :
        answer = '0'
    return answer