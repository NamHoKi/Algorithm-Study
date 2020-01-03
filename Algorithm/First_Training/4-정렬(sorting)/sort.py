import time
import random

global n
n = [1000,10000,100000]

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

def heapify(a,i,heap_size):
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    large_index = i
    if left_index < heap_size and a[left_index] > a[large_index]:
        large_index = left_index
    if right_index < heap_size and a[right_index] > a[large_index]:
        large_index = right_index
    if large_index != i:
        a[large_index] , a[i] = a[i] , a[large_index]
        heapify(a,large_index,heap_size)

def heap_sort():
    global n

    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        s = len(x)
        for j in range(s//2-1,-1 ,-1):
            heapify(x, j, s)
        for j in range(s-1,0,-1):
            x[0],x[j] = x[j],x[0]
            heapify(x,0,j)
        print('Heap Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            s = len(x)
            for j in range(s // 2 - 1, -1, -1):
                heapify(x, j, s)
            for j in range(s - 1, 0, -1):
                x[0], x[j] = x[j], x[0]
                heapify(x, 0, j)
            sum += time.time() - start
        print('Heap Random', n[i], ':', sum / 10)

def library_sort():
    global n

    for i in range(0, len(n)):
        x = create_reverse_data(n[i])
        start = time.time()
        x.sort()
        print('Library Reverse', n[i], ':', time.time() - start)

    for i in range(0, len(n)):
        sum = 0
        for l in range(0, 10):
            x = create_random_data(n[i])
            start = time.time()
            x.sort()
            sum += time.time() - start
        print('Library Random', n[i], ':', sum / 10)

heap_sort()
library_sort()