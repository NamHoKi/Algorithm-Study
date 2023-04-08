def solution(nums):
    n1 = len(nums) // 2
    n2 = len(set(nums))
    if n1 <= n2 :
        return n1
    return n2