def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j指手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort1(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


def shellSort2(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


li = [7, 2, 5, 3, 4, 6, 9, 8, 1, 10]
shellSort2(li)
print(li)
