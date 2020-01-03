# python 3.7.3 -* encoding = 'UTF-8' *-

n,A,B = int(input()),input().split(),input().split()

sum = 0
b = pow(2,28)-1
for i in range(0,n):
    for j in range(0,n):
        sum += int(A[i]) & int(B[j])
        b &= int(A[i]) + int(B[j])

print(sum%1999,b)