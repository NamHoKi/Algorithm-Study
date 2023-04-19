def recursion(word):
    if len(word) == 5 :
        return

    global answer
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for a in alpha :
        answer.append(word + a)
        recursion(word + a)
        
    


def solution(word):
    global answer
    answer = []
    recursion('')
    return answer.index(word) + 1