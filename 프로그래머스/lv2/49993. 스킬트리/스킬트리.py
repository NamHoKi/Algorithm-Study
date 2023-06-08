def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        i = 0
        for t in tree :
            if t in skill :         # 조건있는 스킬이라면
                if skill[i] != t :  # 순서 조건에 맞지 않다면, break
                    break
                else :
                    i += 1
            if t == tree[-1] or i == len(skill):
                answer += 1
                break
    return answer