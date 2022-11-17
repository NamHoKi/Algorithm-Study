from itertools import permutations
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    permutations_list = list(permutations(list(numbers), len(numbers)))
    num_list = []
    for t in permutations_list:
        num_list.append(int(''.join(list(t))))
    num_list = set(num_list)
    for number in numbers:
        if is_prime_number(int(number)): answer += 1

    return answer
