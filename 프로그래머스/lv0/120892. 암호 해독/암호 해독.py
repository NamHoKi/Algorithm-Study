def solution(cipher, code):
    cnt = 0
    answer = ''
    for c in cipher :
        cnt += 1
        if cnt == code :
            answer += c
            cnt = 0
    return answer