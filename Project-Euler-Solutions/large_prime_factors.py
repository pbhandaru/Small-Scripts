#!/usr/bin/python
#############

def large_prime_factor(num):
    primes = []
    odd = 3
    mx = num ** 0.5
    while num % 2 == 0:
        primes.append(2)
        num /= 2

    while odd <= mx:
        while num % odd == 0:
            primes.append(odd)
            num /= odd
            mx = num ** 0.5

        odd += 2

    if num > 2:
        primes.append(num)

    return max(primes)

print large_prime_factor(600851475143)
