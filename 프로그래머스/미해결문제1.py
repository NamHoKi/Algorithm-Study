# https://school.programmers.co.kr/learn/courses/30/lessons/81302#qna
# 2021 카카오 체용연계형 인턴쉽 문제
# 테스트케이스 3, 4, 14, 16, 27, 28, 29, 30 미해결 - 원인조차 알 수 없음
# DFS, BFS보다 if문이 더 효율적이라 생각함 (경우의 수가 적기 때문)


def check_p2p(place, r1, c1, r2, c2):
    d = 0
    if r1 >= r2:
        d += r1 - r2
    else:
        d += r2 - r1
        
    if c1 >= c2:
        d += c1 - c2
    else:
        d += c2 - c1
        
    if d <= 1:
        return True
    elif d == 2:
        if r1 == r2 and place[r1][(c1 + c2) // 2] == 'X':
            return False
        elif c1 == c2 and place[(r1 + r2) // 2][c1] == 'X':
            return False
        elif place[r1][c2] == 'X' and place[r2][c1] == 'X':
            return False
        else:
            return True
    return False


def get_p_list(place):
    p_list = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_list.append([i, j])     
    return p_list    


def solution(places):
    answer = []
    
    for place in places:
        p_list = get_p_list(place)
        if len(p_list) == 0:
            answer.append(1)
        else:
            for i in range(len(p_list) - 1):
                break_check = False
                
                for j in range(i + 1, len(p_list)):
                    if check_p2p(place, p_list[i][0], p_list[i][1], p_list[j][0], p_list[j][1]):
                        answer.append(0)
                        break_check = True
                        break
                        
                    if i == len(p_list) - 2 and j == len(p_list) - 1:
                        answer.append(1)
                if break_check:
                    break
    return answer
