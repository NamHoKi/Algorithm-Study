def solution(k, score):
    answer = []
    k_list = []
    
    for s in score:
        k_list.append(s)
        k_list.sort(reverse=True)
        if len(k_list) > k :
            k_list.pop(-1)
        answer.append(k_list[-1])
    
    return answer