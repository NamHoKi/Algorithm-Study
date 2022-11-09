def solution(food):
    answer = '0'
    
    for i in range(len(food)-1, 0, -1):
        n = food[i] // 2
        if n != 0:
            for j in range(n):
                answer = str(i) + answer + str(i)
        
    return answer