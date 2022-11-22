def solution(elements):
    answer, n = [], len(elements)
    elements = elements + elements
    
    for i in range(n):
        for j in range(1, n + 1):
            answer.append(sum(elements[i:i + j]))
    
    return len(set(answer))