import math
import copy
from datetime import datetime
global tour_list,best_list, best_distance
tour_list = []
best_list = []
best_distance = 1000

def read_file():
    file_name = input('파일이름을 입력하시오 : ')
    with open(file_name,'r',encoding='UTF8') as f:
        global n, x_list, y_list , tour_list
        text = f.read()
        line = text.split('\n')
        n = int(line[0])  # 첫 줄의 첫 원소 = n
        x_list = []
        y_list = []
        for i in range(1,n+1):
            token = line[i].split()
            x_list.append(int(token[0]))
            y_list.append(int(token[1]))
        for i in range(0,n):
            tour_list.append(i)

def swap(k,i):
    global x_list,y_list,tour_list
    temp = x_list[k]
    x_list[k] = x_list[i]
    x_list[i] = temp
    temp = y_list[k]
    y_list[k] = y_list[i]
    y_list[i] = temp
    temp = tour_list[k]
    tour_list[k] = tour_list[i]
    tour_list[i] = temp

def tour(k,curdist):
    global n, x_list, y_list,best_distance,tour_list,best_list
    check = 0
    if curdist >= best_distance:
        check = 1
    elif k==n:
        curdist += (((x_list[k-1]-x_list[0])**2) + (y_list[k-1]-y_list[0])**2)**0.5
        if best_distance > curdist:
            best_distance = curdist
            best_list = copy.deepcopy(tour_list)
    for i in range(k, n):
        swap(k,i)
        tour(k+1,curdist + ((((x_list[k] - x_list[k - 1]) ** 2) + ((y_list[k] - y_list[k - 1]) ** 2)) ** 0.5))
        swap(k,i)
read_file()
now = datetime.now()
print('start : %s:%s:%s'%(now.hour,now.minute,now.second))
tour(1,0)
print(best_distance,'\n',best_list)
now = datetime.now()
print('end : %s:%s:%s'%(now.hour,now.minute,now.second))