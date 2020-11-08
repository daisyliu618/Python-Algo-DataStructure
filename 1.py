def recursion1(x):
    if x > 0:
        print(x)
        recursion1(x - 1)


def recursion2(x):
    if x > 0:
        recursion2(x - 1)
        print(x)


# recursion1(5)
# recursion2(5)

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)


def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1


# time complexity O(logn)


def bubble_sort1(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# nums = [random.randint(0,10000) for i in range(1000)]
nums = [6, 4, 3, 2, 1, 5]
print(nums)
bubble_sort1(nums)
print(nums)


def bubble_sort2(nums):
    for i in range(len(nums) - 1):
        exchange = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        if not exchange:
            return


# nums = [random.randint(0,10000) for i in range(1000)]
# bubble_sort2(nums)
# print(nums)

def select_sort_simple(nums):
    nums_new = []
    for i in range(len(nums)):
        min_val = min(nums)
        nums_new.append(min_val)
        nums.remove(min_val)
    print(nums_new)
    return nums_new


def select_sort(nums):
    for i in range(len(nums) - 1):
        min_loc = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_loc]:
                min_loc = j
        nums[i], nums[min_loc] = nums[min_loc], nums[i]
    return nums


# nums = [6,4,5,3,1,2]
# select_sort(nums)
# print(nums)


def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp


# time complexity 0(n^2)
nums = [6, 4, 5, 3, 1, 2]
insert_sort(nums)
print(nums)


# page 14

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= tmp:
            left += 1

        li[right] = li[left]

    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li, 0, len(li) - 1)
print(li)

# time complexity  O(nlogn) 全部是倒序会达到递归最大深度且最坏是o(n^2)
