def solution(operations):
    x = []
    for s in operations:
        a = s.split(' ')
        if a[0] == "I":
            x.append(int(a[1]))
            if len(x) >= 2:
                x.sort()
        else:
            if len(x) == 0:
                continue
            if a[1] == '1':
                x.pop()
            elif a[1] == '-1':
                x.pop(0)
            else:
                d = int(a[1])
                for i in len(x):
                    if x[i] == d:
                        x.pop(i)
    if len(x) == 0:
        return 0,0
    elif len(x) == 1:
        return x[0], x[0]
    else:
        return max(x), min(x)