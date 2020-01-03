import math

global edge_size
edge_size = 0
node_list = [] # 인접 리스트
weight_list = []
hash = {}
set_list = []

class Node(object):
    def __init__(self,name,longitude,latitude):
        self.name = name
        self.lon = longitude
        self.lat = latitude
        self.adjacecy_list = []
        self.index = None
        self.par = None
        self.size = 1 # 트리 크기

class weight_node(object):
    def __init__(self,u,v):
        self.u = u
        self.v = v
        self.weight = None

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
            node_list.append(node)
        else:
            node[1] = float(node[1])
            node[2] = float(node[2])
            node = Node(node[0],node[1],node[1])
            hash[node.name] = i
            node_list.append(node)

    with open('roadList2.txt','r',encoding='UTF-8') as f:
        text = f.read().split('\n')

    # text의 첫줄 split이 제대로 되지 않아서 첫줄은 수동으로 입력했습니다.
    temp = weight_node(hash['River Square Plaza Shopping Center'],hash['Westfield Number 1 School (historical)'])
    temp.weight = calDistance(node_list[0].lat,node_list[0].lon,node_list[13786].lat,node_list[13786].lon)
    weight_list.append(temp)
    for i in range(1,len(text)):
        token = text[i].split('\t')
        u = hash[token[0]]
        v = hash[token[1]]
        w = calDistance(node_list[u].lat,node_list[u].lon,node_list[v].lat,node_list[v].lon)
        temp = weight_node(u,v)
        temp.weight = w
        weight_list.append(temp)

    for i in range(0,len(weight_list)):
        node_list[weight_list[i].u].adjacecy_list.append(weight_list[i].v)

def path_compression(u):
    if u.par is None:
        return u
    else:
        p = u
        des = []
        while(True):
            if p.par is None:
                for i in range(0,len(des)):
                    des[i].par = p
                return p
            else:
                des.append(p)
                p = p.par

def find_set(target):
    return path_compression(target)

def weighted_union(u,v):
    x = find_set(u)
    y = find_set(v)
    if x.size >= y.size:
        y.par = x
        x.size = y.size + x.size
    else:
        x.par = y
        y.size = y.size + x.size

def kruskal():
    sorted(weight_list, key=lambda weight_node: weight_node.weight) # weight 기준 정렬
    for i in range(0,len(weight_list)):
        u = node_list[weight_list[i].u]
        v = node_list[weight_list[i].v]
        if find_set(u) is not find_set(v):
            weighted_union(u,v)

def main():
    read_file()
    kruskal()
    with open('MST_output.txt','w',encoding='UTF-8') as f:
        for i in range(0,len(node_list)):
            if len(node_list[i].adjacecy_list) is not 0:
                f.write(str(hash[node_list[i].name]) + ' ' + str(node_list[i].lon) + ' ' + str(node_list[i].lat) + ' ' + str(len(node_list[i].adjacecy_list)) + ' ' + str(node_list[i].adjacecy_list) + '\n')

main()