def solution(array, commands):
    answer = []
    for command in commands:
        find_array = array[command[0] - 1:command[1]]
        find_array.sort()
        answer.append(find_array[command[2]-1])
    return answer
