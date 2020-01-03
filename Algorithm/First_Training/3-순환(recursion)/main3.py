import time
import random

global n ,x
n = [1000,10000,100000]
x = []

#랜덤 수 n개 생성
def create_random_data(n):
    a = []
    for i in range(0, n):
        a.append(int((random.random()) * 10000))
    return a
#역순 수 n개 생성
def create_reverse_data(n):
    a = []
    for i in range(0, n):
        a.append(n-i)
    return a
#배열 전역변수로 생성
def create_reverse_x(n):
    global x
    del x[:]
    x = create_reverse_data(n)
def create_random_x(n):
    global x
    del x[:]
    x = create_random_data(n)


#버블정렬
def bubble():
    global n
    for i in range(0,len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        for j in range(n[i],-1,-1):
            for k in range(0,j-1):
                if x[k] > x[k+1]:
                    x[k], x[k + 1] = x[k + 1], x[k]
        print('Bubble Reverse',n[i] ,':',time.time() - start)

    for i in range(0,len(n)):
        sum = 0
        for l in range(0,10):
            x = create_random_data(n[i])
            start = time.time()
            for j in range(n[i],-1,-1):
                for k in range(0,j-1):
                    if x[k] > x[k+1]:
                        x[k], x[k + 1] = x[k + 1], x[k]
            sum+= time.time() - start
        print('Bubble Random',n[i],':' ,sum/10)

#선택정렬
def selection():
    global n
    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        for j in range(n[i]-1, -1, -1):
            index = 0
            for k in range(0, j+1):
                if x[index] < x[k]:
                    index = k
            x[index], x[j] = x[j], x[index]
        print('Selection Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            for j in range(n[i]-1,-1,-1):
                index = 0
                for k in range(0,j+1):
                    if x[index] < x[k]:
                        index = k
                x[index], x[j] = x[j], x[index]
            sum += time.time() - start
        print('Selection Random', n[i], ':', sum / 10)

#삽입정렬
def insertion():
    global n
    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        for j in range(1,n[i]):
            for k in range(j,0,-1):
                if x[k] < x[k-1]:
                    x[k],x[k-1] = x[k-1],x[k]
                else:
                    break
        print('Insertion Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            for j in range(1, n[i]):
                for k in range(j, 0, -1):
                    if x[k] < x[k - 1]:
                        x[k], x[k - 1] = x[k - 1], x[k]
                    else:
                        break
            sum += time.time() - start
        print('Insertion Random', n[i], ':', sum / 10)

#합병정렬
def merge(result):
    if len(result) > 1:
        m = int(len(result) / 2)
        left_arry , right_arry = result[:m] , result[m:]
        left_arry = merge(left_arry)
        right_arry = merge(right_arry)
        left_index, right_index = 0 , 0
        del result[:]
        while len(left_arry) > left_index and len(right_arry) > right_index:
            if left_arry[left_index] < right_arry[right_index]:
                result.append(left_arry[left_index])
                left_index += 1
            else:
                result.append(right_arry[right_index])
                right_index += 1
        if left_index == len(left_arry):
            result += right_arry[right_index:]
        else:
            result += left_arry[left_index:]
    return result

def merge_print():
    global n
    for i in range(0, len(n)):
        x = create_inverse_data(n[i])
        start = time.time()
        merge(x)
        print('Merge Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            merge(x)
            sum += time.time() - start
        print('Merge Random', n[i], ':', sum / 10)

#빠른정렬(마지막 값 pivot)
def partiton1(a,p,r):
    x = a[r]
    i = p - 1
    for j in range(p,r):
         if a[j] <= x:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

def quick1(a,p,r):
    if p<r:
        q = partiton1(a,p,r)
        quick1(a,p,q-1)
        quick1(a,q+1,r)

def quick1_print():
    global n,x
    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        quick1(x, 0, len(x)-1)
        print('Quick1 Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            quick1(x, 0, len(x)-1)
            sum += time.time() - start
        print('Quick1 Random', n[i], ':', sum / 10)

#빠른정렬(중간 값 pivot)
def quick2_print():
    global n
    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        if (x[0] <= x[int(len(x)/2)] and x[int(len(x)/2)] <= x[len(x)-1]) or (x[0] >= x[int(len(x)/2)] and x[int(len(x)/2)] >= x[len(x)-1]):
            x[int(len(x) / 2)] , x[len(x)-1] = x[len(x)-1],x[int(len(x)/2)]
        elif (x[int(len(x)/2)] <= x[0] and x[0] <= x[len(x)-1]) or (x[int(len(x)/2)] >= x[0] and x[0] >= x[len(x)-1]):
            x[0],x[len(x)-1] = x[len(x)-1],x[0]
        quick1(x, 0, len(x)-1)
        print('Quick2 Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            if (x[0] <= x[int(len(x) / 2)] and x[int(len(x) / 2)] <= x[len(x) - 1]) or (
                    x[0] >= x[int(len(x) / 2)] and x[int(len(x) / 2)] >= x[len(x) - 1]):
                x[int(len(x) / 2)], x[len(x) - 1] = x[len(x) - 1], x[int(len(x) / 2)]
            elif (x[int(len(x) / 2)] <= x[0] and x[0] <= x[len(x) - 1]) or (
                    x[int(len(x) / 2)] >= x[0] and x[0] >= x[len(x) - 1]):
                x[0], x[len(x) - 1] = x[len(x) - 1], x[0]
            quick1(x, 0, len(x)-1)
            sum += time.time() - start
        print('Quick2 Random', n[i], ':', sum / 10)

#빠른정렬(랜덤 값 pivot)
def quick3_print():
    global n
    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        random_index = random.randrange(0, len(x) - 1)
        x[random_index], x[len(x) - 1] = x[len(x) - 1], x[random_index]
        quick1(x, 0, len(x)-1)
        print('Quick3 Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            random_index = random.randrange(0, len(x) - 1)
            x[random_index], x[len(x) - 1] = x[len(x) - 1], x[random_index]
            quick1(x, 0, len(x)-1)
            sum += time.time() - start
        print('Quick3 Random', n[i], ':', sum / 10)