def mergeSort(li):
    if len(li) > 1:
        mid = len(li)
        L = li[:mid]
        R = li[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                li[k] = L[i]


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右两边有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行完有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
# print(li)


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)
        print(li[low:high + 1])


li = [7, 2, 5, 3, 4, 6, 9, 8, 1, 10]
merge_sort(li, 0, len(li) - 1)
print(li)

# time complexity o(nlogn)
# space complexity o(n)

"""
一般情况下 快速排序《 归并排序 《 堆排序
缺点：
快速排序：极端情况下排序效率低（倒序）
归并：需要额外的内存开销
堆排序：在快的排序种最慢
稳定排序：冒泡 插入 归并
"""
