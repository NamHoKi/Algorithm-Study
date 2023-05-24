def solution(n):
    x, i = 1, 1
    while True :
        x *= i
        if x > n :
            return i - 1
        i += 1