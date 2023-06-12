def solution(arr, k):
    answer = []
    if k % 2 == 0 :
        for a in arr :
            answer.append(a + k)
    else :
        for a in arr :
            answer.append(a * k)
    return answer