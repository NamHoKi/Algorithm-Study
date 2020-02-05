def solution(begin, target, words):
    answer = 0
    def DFS(target,words,cnt):
        if not (target in words):
            return 0
        if target in words:
            return cnt + 1
        for i in range(len(words)):

    return answer

#####
