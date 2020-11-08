def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    print(count)
    for c in li:
        count[c] += 1
    li.clear()
    print(count)
    for index, value in enumerate(count):
        for j in range(value):
            li.append(index)


li = [7, 2, 5, 3, 4, 6, 9, 8, 1, 10]
count_sort(li)
print(li)

"""
只适用于正整数排序
time compelxity o(n)
"""
