class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    # 头插法
    def creat_linklist(li):
        head = Node(li[0])
        for element in li[1:]:
            node = Node(element)
            node.next = head
            head = node
        return head

    # 尾插法
    def creat_linkedlist_tail(li):
        head = Node(li[0])
        tail = head
        for element in li[1:]:
            node = Node(element)
            tail.next = node
            tail = node
        return head

    def print_linklist(lk):
        while lk:
            print(lk.item, end=',')
            lk = lk.next


    @staticmethod
    def insertSingleLk(p, curNode):
        p.next = curNode.next
        curNode.next = p

    @staticmethod
    def deleteSingleLK(p, curNode):
        p: object = curNode.next
        curNode.next = curNode.next.next
        del p


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

lk = Node.creat_linklist([1, 2, 3, 4])
Node.print_linklist(lk)


# 双链表
class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prior = None

    @staticmethod
    def insertDoubleLK(self, curNode, p):
        p.next = curNode.next
        curNode.next.prior = p
        p.prior = curNode
        curNode.next = p

    @staticmethod
    def deleteDoubleLK(self, curNode, p):
        p = curNode.next
        curNode.next = p.next
        p.next.prior = curNode
        del p

