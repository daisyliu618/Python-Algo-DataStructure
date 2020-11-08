def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var放到几号桶里
        buckets[i].append(var)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


# li = [7, 2, 5, 3, 4, 6, 9, 8, 1, 10]
# li = bucket_sort(li)
# print(li)

def radix_sort(li):
    max_num = max(li) #最大值
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写会li
        it += 1

li = [7, 2, 5, 3, 4, 6, 9, 8, 1, 10]
radix_sort(li)
print(li)

"""
桶排序 time complexity o(n)
基数排序time complexity o(kn)
"""