#!/usr/bin/python
import re
#####################
digits = {}
with open('count_digits.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        ls = list(line)
        for i in range(0,10):
            for d in ls:
                m = re.match('\S', d)
                if m:
                    if not i in digits:
                        if int(d) == i:
                            digits[i] = 1
                        else:
                            digits[i] = 0
                    else:
                        if int(d) == i:
                            digits[i] += 1
                            continue

#
print digits
