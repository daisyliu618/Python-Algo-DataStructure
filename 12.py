class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.leftChild = a
e.rightChild = g
a.rightChild = c
c.leftChild = b
c.rightChild = d
g.rightChild = f
root = e


# print(root.leftChild.rightChild.data)


def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.leftChild)
        pre_order(root.rightChild)


def in_order(root):
    if root:
        in_order(root.leftChild)
        print(root.data, end=",")
        in_order(root.rightChild)


def post_order(root):
    if root:
        post_order(root.leftChild)
        post_order(root.rightChild)
        print(root.data, end=",")


from collections import deque


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=",")
        if node.leftChild:
            queue.append(node.leftChild)
        if node.rightChild:
            queue.append(node.rightChild)


pre_order(root)
print("=======")
in_order(root)
print("=======")
post_order(root)
print("=======")
level_order(root)

#pre-oder类似于DFS
#要通过序列确认一棵树 一定要有中序