def solution(n):
    answer = 1
    for i in range(1, (n // 2) + 2) :
        temp_sum = i
        for j in range(i + 1, n + 1) :
            temp_sum += j
            if temp_sum == n :
                answer += 1
            if temp_sum > n :
                break
    return answer