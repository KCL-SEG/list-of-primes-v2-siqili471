"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if number_of_primes > 0:
        while number_of_primes > 0:
            if is_prime(count):
                list.append(count)
                number_of_primes -= 1
            count += 1
    else:
        raise ValueError
    return list

def is_prime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
