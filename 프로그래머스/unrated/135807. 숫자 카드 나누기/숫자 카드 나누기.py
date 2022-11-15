def get_gcd(a, b):
    while b != 0 :
        a, b = b, a % b

    return a

def check_div(a, gcd):
    for num in a:
        if num % gcd == 0:
            return 0
    return gcd
    
def solution(arrayA, arrayB):
    a_gcd, b_gcd = arrayA[0], arrayB[0]
    for i in range(len(arrayA)):
        a_gcd = get_gcd(a_gcd, arrayA[i])
    for i in range(len(arrayB)):
        b_gcd = get_gcd(b_gcd, arrayB[i])
    
    ab = check_div(arrayB, a_gcd)
    ba = check_div(arrayA, b_gcd)
    
    if ab > ba:
        return ab
    return ba
