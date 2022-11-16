class node():
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

def create_tree(triangle):
    head_node = node(triangle[0][0])
    if len(triangle) == 1:
        pass
    else:
        for i in range(0, len(triangle) - 1):
            for j in range(len(triangle[i])):
                if i == 0:
                    cur_node = head_node
                else:
                    cur_node = node(triangle[i][j])
                cur_node.left = node(triangle[i + 1][j])
                cur_node.right = node(triangle[i + 1][j + 1])
    return head_node

def DFS(node, sum):
    print(node.n)
    if node.left == None:
        return sum
    else:
        if DFS(node.left, sum) + sum >= DFS(node.right, sum) + sum:
            return left + sum
        return right + sum
    
    
def solution(triangle):
    head_node = create_tree(triangle)
    return DFS(head_node, 0)
