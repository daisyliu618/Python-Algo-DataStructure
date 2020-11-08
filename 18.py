import time


def sieve_of_eratosthenes(n):
    start_time = time.time()
    is_prime = [True] * (n - 1)
    p = 2
    while True:
        multiplier = 2
        multiplier = p * multiplier  # 2p, 3p, 4p
        while multiplier <= n:
            is_prime[multiplier - 2] = False
            multiplier += 1
            multiplier = p * multiplier
        for i, prime in enumerate(is_prime):
            if prime and i + 2 > p:
                p = i + 2
                break
        else:
            break
    end_time = time.time()
    for i, prime in enumerate(is_prime):
        if prime: print(i + 2)

    print("Total time: %0.5f" % (end_time - start_time))


# sieve_of_eratosthenes(100)

# soe
def sieve_of_eratosthenes2(n):
    prime = [True] * n
    multiplier = 2
    while multiplier <= (int(n ** 0.5)):
        multiple = 2 * multiplier

        while multiple < n:
            prime[multiple] = False
            multiple += multiplier
        multiplier += 1

    i = 2
    while i < n:
        if prime[i] == 1:
            print(i)
        i += 1


sieve_of_eratosthenes2(99)
