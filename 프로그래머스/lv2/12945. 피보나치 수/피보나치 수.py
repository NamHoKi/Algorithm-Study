def solution(n):
    answer = 0
    f0, f1, = 0, 1
    f2 = f0 + f1
    
    for i in range(n - 2) :
        f0, f1 = f1, f2
        f2 = f0 + f1
        
    return f2 % 1234567