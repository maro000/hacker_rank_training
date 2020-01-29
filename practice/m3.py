# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = list(map(str, input().replace(".",' ').split(' ')))
# print(n)
a =list(set(n))
# print(a)
count = 0
for i in range(len(a)):
    if re.search('[A-Z]',a[i]) or re.search('[0-9]',a[i]):
        count += 1
print(count)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = list(map(int,input().split(',')))
n.sort()

l = []
for i in range(len(n)):
    if i % 2 == 1:
        l.append(n[i])
    elif n[i] == n[i-1]:
        l.append(n[i])

a = ','.join(map(str,l))
print(a)