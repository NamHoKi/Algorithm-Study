# python 3.7.3 -* encoding = 'UTF-8' *-

n = int(input())
str_list = []
palindrome_list = []

def find_palindrome(str):
    p = []
    for i in range(0,len(str)):
        for j in range(i+1,len(str)):
            x = str[i:j+1]
            if x == x[::-1]:
                p.append(x)
    return p

def find_common_longest_str(palindrome_list):
    com_list = palindrome_list[0]
    for i in range(1,len(palindrome_list)):
        com_list = list(set(com_list) & set(palindrome_list[i]))
    com_list.sort(key=len)
    if len(com_list) == 0:
        print('0')
        return
    else:
        print(len(com_list[0]))

for i in range(0,n):
    str_list.append(input())
    palindrome_list.append(find_palindrome(str_list[i]))
find_common_longest_str(palindrome_list)