# python 3.7.3 -* encoding = 'UTF-8' *-

s = input()
x = 'UCPC'
j = 0
for i in range(0,len(s)):
    if s[i] == x[j]:
        j += 1
        if j == 4:
            print('I love UCPC')
            break
    if i == len(s) - 1:
        print('I hate UCPC')