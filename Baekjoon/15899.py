# python 3.7.3 -* encoding = 'UTF-8' *-
# 부모,자식 순으로 입력

tree = []
sum = 0

class Node(object):
    def __init__(self,color = None):
        self.next = []
        self.color = color

def f(p,c,cnt):
    if p is None:
        return
    if p.color <= c:
        cnt += 1
    for i in range(0,len(p.next)):
        cnt = f(p.next[i],c,cnt)
    return cnt

tree.append(Node(-1))
n,m,c = map(int,input().split())
color = input().split()

for i in range(0,n):
    tree.append(Node(int(color[i])))

for i in range(0,n-1):
    a,b = map(int,input().split())
    tree[a].next.append(tree[b])

for i in range(0,m):
    a,b = map(int, input().split())
    sum += f(tree[a],b,0)

print(sum)
