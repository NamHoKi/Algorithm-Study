# python 3.7.3 -* encoding = 'UTF-8' *-

L = int(input())
n1 = int(input())
a1 = input().split()
n2 = int(input())
a2 = input().split()

l1,l2,i1,i2,merge_cnt,split_cnt = 0,0,0,0,0,0

while(l1 < L or l2 < L):
    if l1 == l2:
        l1 += int(a1[i1])
        i1 += 1
        l2 += int(a2[i2])
        i2 += 1
    else:
        if l1 < l2:
            l1 += int(a1[i1])
            i1 += 1
            merge_cnt += 1
        else:
            l2 += int(a2[i2])
            i2 += 1
            split_cnt += 1
print(merge_cnt + split_cnt)