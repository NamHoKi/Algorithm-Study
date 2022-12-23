from itertools import permutations

def solution(k, dungeons):
    all_list = list(permutations(dungeons, len(dungeons)))
    answer = -1
    
    for p_tuple in all_list:
        cur_k = k
        cur_cnt = 0
        for p_list in p_tuple:
            need, consume = p_list[0], p_list[1]
            if cur_k >= need and cur_k >= consume:
                cur_k -= consume
                cur_cnt += 1
            else:
                break
        
        if answer < cur_cnt :
            answer = cur_cnt
                
    return answer