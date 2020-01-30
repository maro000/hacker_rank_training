n = int(input())

l = [list(map(str, input().split())) for _ in range(n)]

print(l)
x = 0
y = 0

for i in range(n):
    if l[i][0] == 'SET':
        if int(l[i][1]) == 1:
            x = int(l[i][2])
        elif int(l[i][1]) == 2:
            y = int(l[i][2])

    if l[i][0] == 'ADD':
        y = x + int(l[i][1])

    if l[i][0] == 'SUB':
        y = x - int(l[i][1])

print(x,y)