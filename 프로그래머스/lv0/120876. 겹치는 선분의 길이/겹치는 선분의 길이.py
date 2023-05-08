from collections import Counter

def solution(lines):
    l, answer = [], 0
    for start, end in lines :
        l += [i for i in range(start, end)]
    
    c = Counter(l)
    for k, v in c.items() :
        if v > 1 :
            answer += 1            

    return answer