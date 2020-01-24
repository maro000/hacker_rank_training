#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valleys_count = 0
    for direction in s:
        if direction == 'U':
            level += 1
            if level == 0:
                valleys_count += 1
        else:
            level -= 1
    return valleys_count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()

print(countingValleys)