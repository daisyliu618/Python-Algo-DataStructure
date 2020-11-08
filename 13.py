class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_recursion(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.leftChild = self.insert(node.leftChild, val)
        elif val > node.data:
            node.rightChild = self.insert(node.rightChild, val)
        return node

    def insert_no_recursion(self, val):
        pointer = self.root
        if not pointer:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < pointer.data:
                if pointer.leftChild:
                    pointer = pointer.leftChild
                else:
                    pointer.leftChild = BiTreeNode(val)
                    pointer.leftChild.parent = pointer
                    return
            elif val > pointer.data:
                if pointer.rightChild:
                    pointer = pointer.rightChild
                else:
                    pointer.rightChild = BiTreeNode(val)
                    pointer.rightChild.parent = pointer
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rightChild, val)
        elif node.data > val:
            return self.query(node.leftChild, val)
        else:
            return node

    def query_no_recursion(self, val):
        pointer = self.root
        while pointer:
            if pointer.data < val:
                pointer = pointer.rightChild
            elif pointer.data > val:
                pointer = pointer.leftChild
            else:
                return pointer
        return None

    @staticmethod
    def minValueNode(node):
        current = node
        while current.leftChild:
            current = current.leftChild
        return current

    #改用值覆盖 把要删除的节点的值覆盖成他的子节点的值 然后删除子节点的值 然后一直这样递归
    def delete(self, node, val):
        if node is None:
            return None
        else:  # 不是空树
            node1 = self.query_no_recursion(val)
            if not node1:  # 不存在
                return
            if val < node.data:
                node.leftChild = self.delete(node.leftChild, val)
            elif val > node.data:
                node.rightChild = self.delete(node.rightChild, val)
            else:
                if node.leftChild is None and node.rightChild is not None:
                    # temp = node.rightChild
                    # node = None
                    node.data = node.rightChild.data
                    node.rightChild = node.rightChild.rightChild if node.rightChild.rightChild is not None else node.rightChild.leftChild
                    return node
                elif node.rightChild is None and node.leftChild is not None:
                    node.data = node.leftChild.data
                    node.leftChild = node.leftChild.leftChild if node.leftChild.leftChild is not None else node.leftChild.rightChild
                    return node
                elif node.leftChild is not None and node.rightChild is not None:
                    temp = self.minValueNode(node.rightChild)
                    node.data = temp.data
                    node.rightChild = self.delete(node.rightChild, temp.data)
                else:
                    return None

        return node

    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.leftChild)
            self.pre_order(root.rightChild)

    def in_order(self, root):
        if root:
            self.in_order(root.leftChild)
            print(root.data, end=",")
            self.in_order(root.rightChild)

    def post_order(self, root):
        if root:
            self.post_order(root.leftChild)
            self.post_order(root.rightChild)
            print(root.data, end=",")


# tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])

tree = BST([1, 2, 3])

print("pre order")
tree.pre_order(tree.root)
print("in order")
tree.in_order(tree.root)
print("post order")
tree.post_order(tree.root)

# 二叉树的中序序列是有序序列
#
# tree.query(2, 4)
# tree.insert(4)
tree.delete(tree.root, 1)

print("after delete")
tree.in_order(tree.root)


