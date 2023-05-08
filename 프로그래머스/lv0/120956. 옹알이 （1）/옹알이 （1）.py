def solution(babbling):
    answer = 0
    aa = ["aya", "ye", "woo", "ma"]
    
    for b in babbling :
        for a in aa :
            if a in b :
                b = b.replace(a, '*')
            check = b[:]
            if check.replace('*', '') == '' :
                answer += 1
                break

    return answer