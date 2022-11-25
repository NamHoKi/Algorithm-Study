def solution(s):
    stack=[]
    
    for i in range(len(s)):
        c=s[i]
        if len(stack)>0 and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)
    
    if len(stack)==0:
        return 1
    else:
        return 0