def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        y = int((d*d - x*x)**(1/2))
        
        for min_y in range(y, 0, -1):
            if min_y % k == 0:
                y = min_y
                break
        
        answer += (y // k) + 1
    
    return answer