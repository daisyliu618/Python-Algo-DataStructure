import time


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    cache_limit = None
    DEBUG = False  # If DEBUG is equal to TRUE, you will get cache list printed on each and be able to

    # see cached results printed etc

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __call__(self, *args, **kwargs):
        if args in self.cache:
            self.llist(args)
            if self.DEBUG:
                return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
            return self.cache[args]
        # If cache-limit reached - Remove LRU from node link list and dict - cache.
        if self.cache_limit is not None:
            if len(self.cache) > self.cache_limit:
                node = self.head.next
                self._remove(node)
                del self.cache[node.key]

        # Compute and cache and node - if not in cache
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        if self.DEBUG == True:
            return f'{result}\nCache: {self.cache}'
        return result

    # Remove from double linked-list - Node.
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # Add to double linked-list - Node.
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    # If in result in cache, move to top of Cache/linked-list - Node.
    def llist(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                if self.DEBUG == True:
                    del self.cache[node.key]  # Debugging/ to view cache list in order of linked-list...
                    self.cache[node.key] = node.val  # Debugging/ to view cache list in order of linked-list...
                break
            else:
                current = current.next


#test

# Only setting this for testing purpose/testing file.
LRUCache.DEBUG = True  # DEFAULTS to False. When True, will print Cached list per each result, and show in test file
# when result is cached etc... used for debugging/testing purposes only.

LRUCache.cache_limit = 3  # DEFAULTS to None. If None...There is no limit to the cach list. Setting to 3 in test file..


# for testing purposes.

@LRUCache
def ex_func_01(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n * n


@LRUCache
def ex_func_02(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n * n


print(f'\nFunction: ex_func_01')
print(ex_func_01(4))  # Cache: {(4,): 16}
print(ex_func_01(5))  # Cache: {(4,): 16, (5,): 25}
print(ex_func_01(4))  # Cache: {(5,): 25, (4,): 16}
print(ex_func_01(6))  # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7))  # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49}
print(ex_func_01(8))  # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64}

print(f'\nFunction: ex_func_02')
print(ex_func_02(8))  # Cache: {(8,): 64}
print(ex_func_02(7))  # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6))  # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4))  # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16}
print(ex_func_02(5))  # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25}
print(ex_func_02(4))  # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16}


print("Function: ex_func_01")
print(ex_func_01(4))  # Cache: {(4,): 16}
print(ex_func_01(5))  # Cache: {(4,): 16, (5,): 25}
print(ex_func_01(4))  # Cache: {(5,): 25, (4,): 16}
print(ex_func_01(6))  # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7))  # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49}
print(ex_func_01(8))  # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64}

print(f'\nFunction: ex_func_02')
print(ex_func_02(8))  # Cache: {(8,): 64}
print(ex_func_02(7))  # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6))  # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4))  # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16}
print(ex_func_02(5))  # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25}
print(ex_func_02(4))  # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16}


# 参考
# https://www.youtube.com/watch?v=ckK92JcyV1Y
# https://github.com/ncorbuk/Python-LRU-Cache/blob/master/LRUCache_test.py
