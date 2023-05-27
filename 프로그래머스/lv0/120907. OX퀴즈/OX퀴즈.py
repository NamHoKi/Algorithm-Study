def solution(quiz):
    answer = []
    for q in quiz :
        left, right = q.split('=')
        
        if eval(left) == eval(right) :
            answer.append('O')
        else :
            answer.append('X')

    return answer