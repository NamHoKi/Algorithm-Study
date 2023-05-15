# 프로그래머스 문제 코드
<hr>

## 자동 깃허브 커밋되는 확장 프로그램(백준허브 in Chrome) 사용
#### 백준허브 사용법 : [링크](https://velog.io/@flaxinger/%EB%B0%B1%EC%A4%80%ED%97%88%EB%B8%8C-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)

<hr>
# 미해결 문제

https://school.programmers.co.kr/learn/courses/30/lessons/1844

제출했을 때, 실패 (signal: aborted (core dumped)) 오류 ?
```
def dfs(maps, x, y, count) :
    global answer
    try :
        if maps[x][y] == 0 :
            return
    except Exception as e :
        return
    
    if x == len(maps) - 1 and y == len(maps) - 1 :
        if answer == -1 :
            answer = count
        else :
            answer = min(answer, count)
        return
    
    maps[x][y] = 0
    for ox, oy in [[1,0], [0,1], [0,-1], [-1,0]] :
        dfs(maps, x + ox, y + oy, count + 1)
        

def solution(maps):
    global answer
    answer = -1
    dfs(maps, 0, 0, 1)
    return answer
 ```
 
 

 
 안전지대 (lv0) 테스트케이스 하나 불만족
https://school.programmers.co.kr/learn/courses/30/lessons/120866
0이면 주위 8방향1인지 체크,





그리디 - 큰 수 만들기 : 풀다가 중간에 멈춤
https://school.programmers.co.kr/learn/courses/30/lessons/42883

```
def solution(number, k):
    number = list(number)
    k_cnt = 0
    l = len(number)
    del_number = 0
    
    while del_number < 10 :
        i = 0
        while i < l:
            if number[i] == str(del_number) :
                number.pop(i)
                i -= 1
                k_cnt += 1
                l -= 1
                if k_cnt == k :
                    return ''.join(number)
            i += 1
        del_number += 1
```
