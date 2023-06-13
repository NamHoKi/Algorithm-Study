def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix :
        return 1
    return 0