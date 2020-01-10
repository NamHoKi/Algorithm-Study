# 정답
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1
    return answer


## 오답
#시간 초과
def solution1(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer

        a,b = scoville.pop(0),scoville.pop(0)
        scoville.append(a+(b*2))
        scoville.sort()
        answer += 1
    return answer

# 시간 초과 solution1 보다 오래 걸림
from queue import PriorityQueue

def solution2(scoville, K):
    answer = 0
    q = PriorityQueue(1000000)
    for s in scoville:
        q.put(s)

    while True:
        a = q.get()
        if a >= K:
            return answer
        if len(scoville) == 0:
            if a > K:
                return -1
            else:
                return answer
        b = q.get()
        q.put(a+(b*2))
        answer += 1
    return answer
