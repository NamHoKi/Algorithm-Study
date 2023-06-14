from collections import Counter

def solution(n):
    answer = 0
    b = bin(n)[2:]
    c = Counter(b)
    o = c['1']
    
    while True :
        n += 1
        b = bin(n)[2:]
        if Counter(b)['1'] == o :
            return n
    