#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
t = "{0:b}".format(n)
print(max(map(len,t.split("0"))))