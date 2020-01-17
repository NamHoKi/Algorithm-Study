import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    candidates = []
    supplies = [-x for x in supplies]
    while stock < k:
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                idx = i + 1
                heapq.heappush(candidates, supplies[i])
            else:
                break
        stock = stock + heapq.heappop(candidates) * -1
        answer = answer + 1
    return answer
 
