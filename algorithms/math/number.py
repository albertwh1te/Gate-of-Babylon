def is_prime(n: int) -> bool:
    # 1 is not a prime number
    # https://brilliant.org/wiki/is-1-prime/
    if n <= 1:
        return 0
    if n == 2:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        return 1


print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(13))
print(is_prime(35))
print(is_prime(97))
