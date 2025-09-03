def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
    return count

print(count_primes(5))

