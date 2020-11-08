import random
import heapq


def heapify(li, length, root):
    largest = root  # 把i设为最大的
    left = 2 * root + 1
    right = 2 * root + 2
    if left < length and li[root] < li[left]:  # 如果做孩子存在 和左孩子比
        largest = left
    if right < length and li[largest] < li[right]:  # 如果右孩子存在 和右孩子比
        largest = right
    if largest != root:  # 和largest交换
        li[root], li[largest] = li[largest], li[root]
        heapify(li, length, largest)


def heapSort(li):
    length = len(li)
    # build a maxheap
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(length // 2 - 1, -1, -1):
        heapify(li, length, i)

    # One by one extract elements
    for i in range(length - 1, 0, -1):
        li[i], li[0] = li[0], li[i]
        heapify(li, i, 0)


# li = [i for i in range(100)]
#
# random.shuffle(li)
# print(li)

# time complexity o(nlogn)

li = [12, 11, 13, 5, 6, 7]
heapSort(li)
n = len(li)
print('Sorted array is')
for i in range(n):
    print("%d" % li[i])

# page 26
