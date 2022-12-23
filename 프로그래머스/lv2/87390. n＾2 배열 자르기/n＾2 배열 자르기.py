def solution(n, left, right):
    answer = []
    right += 1
    
    for idx in range(left, right):
        i, j = idx //n , idx % n
        answer.append(max([i, j]) + 1)
        
    
    return answer