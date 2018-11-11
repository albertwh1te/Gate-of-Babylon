def prime(n):
    """
    return if n is a prime number
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def fizzbuzz(n):
    # TODO
    fizzbuzzs = ["Fizz", "Buzz"]
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print(fizzbuzzs[0])
        elif i % 5 == 0:
            print(fizzbuzzs[1])
        else:
            print(i)

        if prime(i):
            fizzbuzzs.reverse()
            print(i, fizzbuzzs)


fizzbuzz(10)
