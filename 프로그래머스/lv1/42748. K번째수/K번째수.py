def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        i, k = i - 1, k - 1
        a = array[i:j]
        a.sort()
        answer.append(a[k])
        
    return answer