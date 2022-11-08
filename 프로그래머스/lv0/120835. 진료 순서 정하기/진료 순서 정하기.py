def solution(emergency):
    n = len(emergency)
    answer = [0] * n
    
    sorted_emergency = sorted(emergency)    
    cnt = 0
    
    for min_num in sorted_emergency:
        min_num_index = emergency.index(min_num)
        answer[min_num_index] = n - cnt
        cnt += 1
    
    return answer