def solution(s):
    stack = []
    
    for x in s :
        if stack != [] and x == ')' and stack[-1] == '(' :
            stack.pop(-1)
        else :
            stack.append(x)
                
    if len(stack) == 0 :
        return True
    return False