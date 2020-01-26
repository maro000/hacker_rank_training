#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_1 = s.count('a') * (n//len(s))
    count_2 = s[:n % len(s)].count('a')
    sum = count_1 + count_2
    # count = 0
    # for i in range(n):
    #     if c[i] == 'a':
    #         count += 1
    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
