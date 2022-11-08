# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        complt = []
        pop_list = []
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                complt.append(i)
        if len(complt) != 0 and complt[0] == 0:
            start = -1
            for i in range(len(complt)):
                if start + 1 == complt[i]:
                    start += 1
                    pop_list.append(i)
                else:
                    break
            for i in range(len(pop_list)-1,-1,-1):
                progresses.pop(i)
                speeds.pop(i)
                cnt += 1
            answer.append(cnt)
    return answer