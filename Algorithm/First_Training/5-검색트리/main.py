class Node(object):
    def __init__(self, word, pos, mean):
        self.word = word
        self.pos = pos
        self.mean = mean
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, word, pos, mean):
        self.root = self._insert_value(self.root, word, pos, mean)
        return self.root is not None

    def _insert_value(self, node, word, pos, mean):
        if node is None:
            node = Node(word, pos, mean)
        else:
            if word <= node.word:
                node.left = self._insert_value(node.left, word, pos, mean)
            else:
                node.right = self._insert_value(node.right, word, pos, mean)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None:
            return False
        if root.word == key:
            return root

        elif key < root.word:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False
        deleted = False
        if key == node.word:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.word:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def node_count(self, node):
        if node == None:
            return 0
        return 1 + self.node_count(node.right) + self.node_count(node.left)

BST = BST()
def read_file():
    with open('shuffled_dict.txt','r',encoding='UTF-8') as f:
        text = f.read().split('\n')
        for i in range(0,len(text)):
            node = []
            ws = text[i].split(' (')
            l1 = len(ws[0])
            node.append(ws[0])
            ws = text[i].split(') ')
            l2 = len(ws[0])
            typ = text[i][l1+1:l2+1]
            m = text[i].split(') ')
            node.append(typ)
            if len(m) == 1:
                m.append('Nothing.')
            node.append(m[1])
            BST.insert(node[0],node[1],node[2])

def main():
    read_file()
    while(True):
        command = input('$ ')
        token = command.split()
        if token[0] == 'size':
            print(BST.node_count(BST.root))
        elif token[0] == 'find':
            result = BST.find(token[1])
            if result != False:
                print(result.word + ' ' + result.pos + ' ' + result.mean)
            else:
                print("Not Found.")
        elif token[0] == 'add':
            w1 = input('word : ')
            t1 = '(' + input('class : ') + '.)'
            m1 = input('meaning : ')
            BST.insert(w1,t1,m1)
        elif token[0] == 'delete':
            result = BST.delete(token[1])
            if result:
                print('Deleted successfully.')
            else:
                print('Not found.')
        elif token[0] == 'deleteall':
            with open(token[1],'r',encoding='UTF-8') as df:
                a = BST.node_count(BST.root)
                while(True):
                    del_word = df.readline().split("\n")[0]
                    if not del_word:
                        break
                    BST.delete(del_word)
                b = BST.node_count(BST.root)
                print("%d words were deleted successfully." % int(a - b))
        elif token[0] == 'exit':
            break
        else:
            print('Input Error!')
main()