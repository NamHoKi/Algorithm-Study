def solution(priorities, location):
    cnt = 0
    p = priorities[:]
    while len(p) > 0:
        if max(p) == p[0]:
            p.pop(0)
            cnt += 1
            location -= 1
            if location == -1:
                return cnt
        else:
            location -= 1
            q = p.pop(0)
            p.append(q)
            if location == -1:
                location = len(p) - 1