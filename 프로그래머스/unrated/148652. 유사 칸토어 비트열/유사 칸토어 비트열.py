def solution(n, l, r):
    answer = 0
    for i in range(l-1, r) :
        while True :
            if i % 5 == 2 :
                break
            if i // 5 == 2 :
                break
            if i < 5 :
                answer += 1
                break
            i = i // 5

    return answer