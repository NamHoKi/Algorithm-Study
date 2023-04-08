def solution(clothes):
    dic = {}
    
    # hash
    for c in clothes :
        n, w = c
        if dic == {} :
            dic[w] = [n]
        else :
            if w in list(dic.keys()) :
                dic[w].append(n)
            else :
                dic[w] = [n]
    
    answer = 1
    for v in dic.values() :
        answer *= len(v) + 1
    return answer - 1
    