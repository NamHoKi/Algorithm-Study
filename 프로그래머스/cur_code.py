from itertools import permutations
import math

def is_prime_number(x):
    if x <= 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 2):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):
    answer, num_list = 0, list(numbers)
        
    for i in range(2, len(numbers) + 1):
        permutations_list = list(permutations(list(numbers), i))
        for num_tuple in permutations_list:     # 각 자리수 리스트 -> 문자열 -> 정수
            num_list += [int(''.join(list(num_tuple)))]
            
    num_list = list(set(num_list))              # 중복 제거

    for number in num_list:                     # 소수라면 answer + 1
        answer += is_prime_number(int(number))

    return answer
   
