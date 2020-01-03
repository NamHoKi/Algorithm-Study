# python 3.7.3 -* encoding = 'UTF-8' *-

tree = []
sum =0
n = int(input())

class Node(object):
    def __init__(self):
        self.p = None
        self.child = []

def tree_add(a,b):
    if a == 1:
        tree[a].child.append(b)
        tree[b].p = tree[a]
    elif b == 1:
        tree[b].child.append(a)
        tree[a].p = tree[b]
    else:
        if tree[a].p is None:
            tree[a].p = tree[b]
            tree[b].child.append(a)
        elif tree[b].p is None:
            tree[b].p = tree[a]
            tree[a].child.append(b)

for i in range(0,n+1):
    tree.append(Node())

for i in range(1,n):
    a,b = map(int,input().split())
    tree_add(int(a),int(b))

for i in range(1,n+1):
    if len(tree[i].child) is 0:
        x = tree[i]
        while(x is not tree[1]):
            sum += 1
            x = x.p

if sum%2 is 0:
    print('No')
else:
    print('Yes')