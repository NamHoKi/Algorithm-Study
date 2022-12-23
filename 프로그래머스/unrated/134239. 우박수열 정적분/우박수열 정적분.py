def f(k):
    result = [k]
    while (k > 1):
        if k % 2 == 0:
            k = k // 2
        else:
            k = (k * 3) + 1
        result.append(k)
    return result
            
    
def get_area(y_list):
    result = []
    for i in range(len(y_list) - 1):
        area = (y_list[i] + y_list[i+1]) / 2
        result.append(area)
    return result
    
    
def solution(k, ranges):
    answer = []
    y_list = f(k)
    area_list = get_area(y_list)
    
    for r in ranges:
        r1, r2 = r[0], len(y_list) + r[1] - 1
        if r1 > r2:
            answer.append(-1.0)
        elif r1 == r2:
            answer.append(0.0)
        else:
            answer.append(sum(area_list[r1:r2]))
    return answer