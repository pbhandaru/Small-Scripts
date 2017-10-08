#!/usr/bin/python
#############

def sum_of_3_and_5_multiples(num):
    #return sum([x for x in range(num) if (x % 3 == 0 or x % 5 == 0)])
    multiples = []
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)

    return sum(multiples)

print sum_of_3_and_5_multiples(1000)
