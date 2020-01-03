# python 3.7.3 -* encoding = 'UTF-8' *-
# 입력에 오류가 없다고 가정

n,m = map(int,input().split())
x = input().split()

for i in range(0,n):
    x[i] = int(x[i])

for i in range(0,m):
    x.sort()
    x[0], x[1] = x[0] + x[1], x[0] + x[1]

print(sum(x))