#!/usr/bin/python
###################
def even_fib():
    x = 1
    y = 2
    s = 0
    while True:
        if x % 2 == 0:
            s += x
        x, y = y, x + y
        if x > 4000000:
            break

    return s

print even_fib()
