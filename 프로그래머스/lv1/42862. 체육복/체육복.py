def solution(n, lost, reserve):
    count = 0
    a = [[True]]*7
    print(a)
    a[1] = False
    
    x=[1]
    for i in range(n+2):
        x.append(1)
    
    for i in range(1,n+1):
        if i in lost:
            x[i] -= 1
        if i in reserve:
            x[i] += 1

    for i in range(1,n+1):
        if x[i] == 2:
            if x[i-1] == 0:
                x[i],x[i-1] = 1,1
            elif x[i+1] == 0:
                x[i],x[i+1] = 1,1
    
    for i in range(1,n+1):
        if x[i] >= 1:
            count += 1

    return count