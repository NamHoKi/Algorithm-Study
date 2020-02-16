def solution(citations):
    citations.sort()
    count, h , n = 0, 0, len(citations)    
    for i in range(len(citations)-1, -1 ,-1):
        if i != 0 and citations[i-1] != citations[i] and count >= citations[i]:
            return citations[i]
        count += 1
    return h

## 안되는 케이스가 있음
