def solution(k, tangerine):
    answer = 0
    tangerine_set = set(tangerine)
    tangerine_dic = {}
    
    for key in tangerine_set:
        tangerine_dic[key] = 0
        
    for key in tangerine:
        tangerine_dic[key] += 1
    
    tangerine_sorted_items = sorted(tangerine_dic.items(), key=lambda x:x[1], reverse=True)
    
    for result_tuple in tangerine_sorted_items:
        k -= result_tuple[1]
        answer += 1
        if k <= 0:
            break
    
    return answer