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


def in_order_no_recursion(root):
    res = []
    stack = []
    while stack or root:
        # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        # 这是模拟递归的调用
        if root:
            stack.append(root)
            root = root.leftChild
         # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
          # 然后转向右边节点，继续上面整个过程
        else:
            tmp = stack.pop()
            res.append(tmp.data)
            root = tmp.rightChild
    return res


def in_order_no_extra_space(root):
    res = []
    pre = None
    while root:
        # 如果左节点不为空，就将当前节点连带右子树全部挂到
        # 左节点的最右子树下面
        if root.leftChild:
            pre = root.leftChild
            while pre.rightChild:
                pre = pre.rightChild
            pre.rightChild = root
            # 将root指向root的left
            tmp = root
            root = root.leftChild
            tmp.leftChild = None
        # 左子树为空，则打印这个节点，并向右边遍历
        else:
            res.append(root.data)
            root = root.rightChild
    return res


# pre_order(root)
# print("=======")
# in_order(root)
# print("=======")
# post_order(root)
# print("=======")
# level_order(root)
print("=======")
print(in_order_no_recursion(root))
print("=======")
print(in_order_no_extra_space(root))

# pre-oder类似于DFS
# 要通过序列确认一棵树 一定要有中序


# https://mp.weixin.qq.com/s?__biz=MzI2NDE1MzY3Mw==&mid=2651924984&idx=1&sn=5cc02de31006f9206b3a8de1477da892&chksm=f15576dec622ffc8094cfd43c818473e6a2fa16364a5b0f0c4913bf58fc0063083109e696baa&scene=178&cur_album_id=1377493411015819266#rd
