def solution(clothes):
    keys = [[0,clothes[0][1]]]
    for c in clothes:
        for i in range(len(keys)):
            if keys[i][1] == c[1]:
                keys[i][0] += 1
                break
            if i == len(keys) - 1:
                keys.append([1,c[1]])
    
    if len(keys) == 1:
        return keys[0][0]
    else:
        cnt = 1
        for k in keys:
            cnt *= k[0]+1
        return cnt - 1
