def solution(num_list):
    even, odd = '', ''
    for n in num_list :
        if n % 2 == 0 :
            even += str(n)
        else :
            odd += str(n)
    return int(even) + int(odd)