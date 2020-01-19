def solution(numbers, target):
    if len(numbers) == 0 and target == 0 :
        return 1
    elif len(numbers) == 0:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
