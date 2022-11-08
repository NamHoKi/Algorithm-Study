def solution(s):
    answer = ''
    i = 0
    nums = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    nums_list = [str(x) for x in range(0,10)]
    
    while(1):
        if i >= len(s):
            return int(answer)
        
        if s[i] in nums_list:
            answer += s[i]
            i += 1
            continue

        for j in nums:
            if s[i:].find(nums[j]) == 0:
                answer += nums_list[j]
                i += len(nums[j])
                break