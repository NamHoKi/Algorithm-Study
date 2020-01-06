def solution(phone_book):
    p = sorted(phone_book, key=len)
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            l = len(p[i])
            if p[i] == p[j][:l]:
                return False
    return True
