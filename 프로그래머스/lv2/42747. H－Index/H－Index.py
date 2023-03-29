def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    
    if citations[0] == 0 :
        return 0
    
    for temp_h in range(citations[0], 0, -1) :
        cnt = 0
        for c in citations:
            if c >= temp_h :
                cnt += 1
        if cnt >= temp_h and n - cnt <= temp_h:
            return temp_h
