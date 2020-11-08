class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# q = Queue(5)
# for i in range(5):
#     q.push(i)

from collections import deque


# q = deque()
# q.append(1)  # 队尾进队
# q.popleft()  # 队首出队

# 用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队


#读取文件最后5行
def tail(n):
    with open("test.txt", "r") as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
