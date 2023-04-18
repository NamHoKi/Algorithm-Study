def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1) :
        if yellow % i == 0 :
            w, h = yellow // i, i
            
            if brown == (w + h) * 2 + 4 :
                return [w + 2, h + 2]