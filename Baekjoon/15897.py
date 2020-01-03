# python 3.7.3 -* encoding = 'UTF-8' *-

# n = int(input())
# for i in range(1,n+1):
#     print(i,end='   ')
#     cnt = 0
#     for j in range(1,n+1,i):
#         print(j,end=' ')
#         cnt += 1
#     print('  ///  ' + str(cnt))

n = int(input())
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt += n/i
    else:
        cnt += 1 + n//i
print(int(cnt))