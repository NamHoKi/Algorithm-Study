def solution(num, total):
    if total % num == 0 :
        return [i for i in range((total // num) - (num // 2), (total // num) + (num // 2) + 1)]
    return [i for i in range((total // num) - (num // 2) + 1, (total // num) + (num // 2) + 1)]