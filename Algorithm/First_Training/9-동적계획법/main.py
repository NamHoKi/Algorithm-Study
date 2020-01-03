import math
import heapq

adjacecy_list = [] # 인접 리스트
hash = {}
set = []

class Node(object):
    def __init__(self,name,longitude,latitude):
        self.name = name
        self.lon = longitude
        self.lat = latitude
        self.weight = None
        self.next = None
        self.par = None
        self.value = 9999999999 # 무한대를 표현할 수 없어서 이렇게 했습니다.

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
    adjacecy_list[0].next.weight = calDistance(-86.984440,33.451500,-86.945550,33.482890)
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

def relax(u,x):
    if u is None or x is None:
        return
    if 'x.name' in set:
        return
    if adjacecy_list[hash[x.name]].value > u.value + x.weight:
        adjacecy_list[hash[x.name]].value = u.value + x.weight
        adjacecy_list[hash[x.name]].par = u
        set.append(adjacecy_list[hash[x.name]])

def Dijkstra(s,d):
    q = []
    s.value = 0
    heapq.heappush(q,(s.value,s))
    set.append(s.name)
    while(True):
        if len(q) == 0:
            break
        u = heapq.heappop(q)
        u = u[1]
        next = u.next
        while(True):
            if next is None:
                break
            relax(u,next)
            heapq.heappush(q, (adjacecy_list[hash[next.name]].value , adjacecy_list[hash[next.name]]))
            next = next.next

def main():
    command1 = input('첫 번째 지명 : ')
    command2 = input('두 번째 지명 : ')
    read_file()
    s = adjacecy_list[hash[command1]]
    d = adjacecy_list[hash[command2]]
    Dijkstra(s,d)
    while(True):
        if d.par is None:
            break
        print(d.name)
        d = d.par
        d = adjacecy_list[hash[d.name]]

main()