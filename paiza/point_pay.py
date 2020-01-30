a , b = map(int,input().split(' ')) 
p = 0
cost = []
for i in range(b):
    c = int(input())
    cost.append(c)
    a -= c 
    if p < c:
        p += c // 10 
    elif p >= c:
        p = p - c
        a += c
    print(a,p)
    