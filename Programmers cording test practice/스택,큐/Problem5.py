def solution(arrangement):
    answer = 0
    level = 0
    q = '('
    for p in arrangement:
        if p == '(':
            level += 1
        else:
            level -= 1
            if q == '(':
                answer += level
            else:
                answer += 1
        q = p
    return answer
