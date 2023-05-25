def solution(common):
    if len(common) == 2 :
        return common[1] + (common[1] - common[0])
    elif common[2] - common[1] == common[1] - common[0] :
        return common[-1] + (common[1] - common[0])
    else :
        return common[-1] * (common[1] / common[0])