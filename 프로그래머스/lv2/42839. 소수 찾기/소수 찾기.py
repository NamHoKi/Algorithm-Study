def is_prime_number(x):
    if x <= 1:
        return 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def recursion(cur_number, numbers, index) :
    global number_list
    
    if cur_number != '' :
        number_list.append(cur_number)
        del numbers[index]
    
    if len(numbers) == 0 :
        return
    else :
        for i in range(len(numbers)) :
            recursion(cur_number + numbers[i], numbers[:], i)


def solution(numbers):
    answer = 0
    global number_list
    number_list = []
    numbers = list(numbers)
    
    recursion('', numbers, 0)
    number_set = set(list(map(int, number_list)))
    
    for number in number_set :
        answer +=  is_prime_number(number)

    return answer
    