import random


def heapify(li, length, root):
    smallest = root  # 把i设为最大的
    left = 2 * root + 1
    right = 2 * root + 2
    if left < length and li[root] > li[left]:  # 如果做孩子存在 和左孩子比
        smallest = left
    if right < length and li[smallest] > li[right]:  # 如果右孩子存在 和右孩子比
        smallest = right
    if smallest != root:  # 和largest交换
        li[root], li[smallest] = li[smallest], li[root]
        heapify(li, length, smallest)


def topK(li, k):
    # 建堆
    heap = li[0:k]
    for i in range(k // 2 - 1, -1, -1):
        heapify(heap, k, i)
    print(heap)
    print("===========")
    # 遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            heapify(heap, k, 0)
        print(heap)
    print("===========")
    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)
        print(heap)
    print("===========")
    return heap


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(topK(li, 5))

# li = list(range(1000))
# random.shuffle(li)
# print(topK(li, 5))
