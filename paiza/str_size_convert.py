import math

mn = input().split()

h = int(mn[0])
w = int(mn[1])
x = int(mn[2])

s = ''
for i  in range(h):
    s = s + input()

y = math.ceil(h*w/x)

for t in range(int(y)):
    name = s[0+x*t:x*(t+1)]
    print(name)
     