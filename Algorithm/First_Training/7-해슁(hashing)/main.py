import math
import queue

adjacecy_list = [] # 인접 리스트
hash = {}
output = []

class Node(object):
    def __init__(self,name,longitude,latitude):
        self.name = name
        self.lon = longitude
        self.lat = latitude
        self.weight = None
        self.visited = False
        self.next = None
        self.hop = 0

def deg2rad(deg):
    return (deg*math.pi / 180)


def rad2deg(rad):
    return (rad*180/math.pi)

def calDistance(lat1,lon1,lat2,lon2):
    theta = lon1 - lon2
    dist = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2)) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.cos(deg2rad(theta))
    if not(dist <= 1 and dist >= -1):
        return 0
    dist = math.acos(dist)
    dist = rad2deg(dist)
    dist = dist * 60 * 1.1515
    dist = dist * 1.609344
    dist = dist * 1000
    return dist

def read_file():
    with open('alabama.txt','r',encoding='UTF-8') as f:
        text = f.read().split('\n')

    # text의 첫줄 split이 제대로 되지 않아서 경우를 나눴습니다.
    for i in range(0,len(text)):
        node = text[i].split('\t')
        if len(node) < 3:
            node = node[0].split()
            name = node[0]
            for j in range(1,len(node)-2):
                name = name + ' ' + node[j]
            lon = float(node[len(node)-1])
            lat = float(node[len(node)-2])
            node = Node(name, lon, lat)
            hash[node.name] = i
            adjacecy_list.append(node)

        else:
            node[1] = float(node[1])
            node[2] = float(node[2])
            node = Node(node[0],node[1],node[1])
            hash[node.name] = i
            adjacecy_list.append(node)

    with open('roadList2.txt','r',encoding='UTF-8') as f:
        text = f.read().split('\n')
    check = 0

    # text의 첫줄 split이 제대로 되지 않아서 첫줄은 수동으로 입력했습니다.
    adjacecy_list[0].next = Node('Westfield Number 1 School (historical)',-86.945550,33.482890)
    for i in range(1,len(text)):
        token = text[i].split('\t')
        while(check < len(adjacecy_list)):
            if adjacecy_list[check].name == token[0]:
                break
            else:
                check += 1
        if check >= len(adjacecy_list) - 1:
            return
        for j in range(check,len(adjacecy_list)):
            if token[1] == adjacecy_list[j].name:
                index = j
                temp = Node(adjacecy_list[index].name,adjacecy_list[index].lon,adjacecy_list[index].lat)
                temp.weight = calDistance(adjacecy_list[check].lat,adjacecy_list[check].lon,adjacecy_list[index].lat,adjacecy_list[index].lon)
                temp.next = None
                break
        if adjacecy_list[check].next == None:
            adjacecy_list[check].next = temp
        else:
            next = adjacecy_list[check]
            while(True):
                if next.next == None:
                    next.next = temp
                    break
                else:
                    next = next.next

def BFS_hop(name,max_hop):
    index = hash[name]
    q = queue.Queue()
    cnt = 0
    count = 0
    q.put(adjacecy_list[index])
    adjacecy_list[index].visited = True
    while(True):
        if q.qsize() == 0 or cnt > max_hop:
            break
        else:
            u = q.get()
            cnt += 1
            next = u.next
            while(True):
                if next == None:
                    break
                if adjacecy_list[hash[next.name]].visited == True:
                    next = next.next
                else:
                    print(next.name, next.lat, next.lon)
                    adjacecy_list[hash[next.name]].visited == True
                    q.put(next)
                    next = next.next

# a번을 제대로 구현하지 못했습니다. 주석 해놓은 함수를 사용하면 프로그램이 멈추는데 무슨 이유인지 모르겠습니다.
# def BFS_hop(name,max_hop):
#     index = hash[name]
#     q = queue.Queue()
#     q.put(adjacecy_list[index])
#     adjacecy_list[index].visited = True
#     while(True):
#         u = q.get()
#         if adjacecy_list[hash[u.name]].hop == 10:
#             break
#         next = u.next
#         while(True):
#             if next == None:
#                 break
#             if adjacecy_list[hash[next.name]].visited == True:
#                 next = next.next
#             else:
#                 print(next.name, next.lat, next.lon)
#                 count += 1
#                 adjacecy_list[hash[next.name]].visited == True
#                 adjacecy_list[hash[next.name]].hop = u.hop + 1
#                 q.put(adjacecy_list[hash[next.name]])
#                 next = next.next
#     for i in range(0, len(adjacecy_list)):
#         adjacecy_list[i].hop = 0
#         adjacecy_list[i].par = None
#     return

def DFS(x):
    if x == None:
        return
    index = hash[x.name]
    if adjacecy_list[index].visited == True:
        return
    else:
        adjacecy_list[index].visited = True
        temp = x.name + ' ' + str(x.lat) + ' ' + str(x.lon)
        output.append(temp)
        while(True):
            if x == None:
                break
            else:
                x = x.next
                DFS(x)

def DFS_print():
    name = input('Name : ')
    index = hash[name]
    DFS(adjacecy_list[index])
    for i in range(0,len(adjacecy_list)):
        if adjacecy_list[i].visited == False:
            DFS(adjacecy_list[i])

    with open('output.txt','w',encoding='UTF-8') as f:
        for i in range(0,len(output)):
            f.write(output[i]+'\n')

    for i in range(0,len(adjacecy_list)):
        adjacecy_list[i].visited = False

def main():
    while(True):
        command = input('$ ')
        if command == 'read':
            read_file()
        elif command == 'a':
            name = input('Name : ')
            BFS_hop(name,10)
        elif command == 'b':
            DFS_print()
        elif command == 'exit':
            break
        else:
            print('Input error !')

main()