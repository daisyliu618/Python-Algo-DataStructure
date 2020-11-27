import time

def memoization1(num):
    print('computing...')
    time.sleep(2)
    result = num * num
    return result

cache = {}
def memoization2(num):
    if num in cache:
        print ('cached...')
        return cache[num]

    print('computing...')
    time.sleep(2)
    result = num * num
    cache[num] = result
    return result

print(memoization2(4))
print(memoization2(4))
print(memoization2(4))
print(memoization2(4))


