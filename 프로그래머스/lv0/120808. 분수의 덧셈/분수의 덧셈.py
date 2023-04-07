# def solution(numer1, denom1, numer2, denom2):
#     n1, n2, d = numer1*denom2, numer2*denom1, denom1*denom2
#     n = n1 + n2
    
    
    
#     answer = []
#     return answer
import math

def lcm(a, b):
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = lcm(denom1, denom2)
    
    de1 = denom // denom1
    de2 = denom // denom2
    numer = (numer1 * de1) + (numer2 * de2)
    
    if(math.gcd(numer,denom) != 1 ):
        print (denom)
        print(math.gcd(numer,denom))
        n = numer
        numer = n // math.gcd(n,denom)
        denom = denom // math.gcd(n,denom)
        print(denom)
    
    answer.append(numer)
    answer.append(denom)
    
    
    return answer