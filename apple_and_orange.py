Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@maro000 
sapanz
/
Hackerrank-Problem-Solving-Python-Solutions
11
9579
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights
Hackerrank-Problem-Solving-Python-Solutions/HackerRank-Apple and Orange/Apple_and_Orange.py / 
@sapanz sapanz Solution
f35b434 on 6 Aug 2018
49 lines (33 sloc)  891 Bytes
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

You're using code navigation to jump to definitions or references.
Learn more or give us feedback
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    bcount = 0
    for i in range(len(apples)):
        temp = a+apples[i]
        if(temp in range(s,t+1)):
            acount+=1
    for i in range(len(oranges)):
        temp = b+oranges[i]
        if(temp in range(s,t+1)):
            bcount+=1
    print (acount)
    print (bcount)
        
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)