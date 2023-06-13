def solution(myString, pat):
    myString = myString.replace('A', '#')
    myString = myString.replace('B', '@')
    myString = myString.replace('#', 'B')
    myString = myString.replace('@', 'A')
    
    if pat in myString :
        return 1
    return 0