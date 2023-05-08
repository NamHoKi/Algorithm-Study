def solution(phone_book):
    p_b = sorted(phone_book)
    for i in range(len(p_b) - 1) :    
        if p_b[i] in p_b[i + 1][0:len(p_b[i])]:
            return False
    return True