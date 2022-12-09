# https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 테스트케이스 1만 만족, 나머지 만족하지 않는 이유를 모르겠음
# '질문하기' 에 있는 답변을 봤지만 이미 처리한 예외들 뿐임

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
        big, small = max(y_list[i:i + 2]), min(y_list[i:i + 2])
        area = small + ((big - small) * 0.5)
        result.append(area)
    return result
    
    
def solution(k, ranges):
    answer = []
    y_list = f(k)
    area_list = get_area(y_list)
    
    for r in ranges:
        r1, r2 = r[0], k + r[1]
        if r1 > r2:
            answer.append(-1)
        elif r1 == r2:
            answer.append(0)
        else:
            answer.append(sum(area_list[r1:r2]))
    
    return answer
