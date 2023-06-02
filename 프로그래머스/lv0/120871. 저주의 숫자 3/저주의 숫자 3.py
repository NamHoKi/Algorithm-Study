def solution(n):
    answer = 0
    cnt = 0
    while True :
        if cnt == n :
            return answer
        answer += 1
        if answer % 3 == 0 or '3' in str(answer):
            continue
        else :
            cnt += 1