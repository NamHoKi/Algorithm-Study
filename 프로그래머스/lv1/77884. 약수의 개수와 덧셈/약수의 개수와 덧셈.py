def f(n):
    if n < 1 :
        return 0
    
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0 :
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        if f(n) % 2 == 0:
            answer += n
        else:
            answer -= n
    
    return answer