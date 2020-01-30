l = []
for i in range(5):
    a = int(input())
    l.append(a)
for i in range(4):
    days = l[i+1] - l[i]
    print(days)

n = int(input())
print(n//2)

a , b = map(int,input().split(' '))
if  (a*b) <= 9999:
    print(a*b)

a = 0
for i in range(int(input())):
    a += (i+1)

print(a)

n = int(input())
if n % 2 == 0:
    print('even')
else:
    print('odd')

a , b , c ,d = map(int,input().split(' '))
s = ((a*d)-(b*c))//2

if (a % 2 == 1) and (b % 2 == 0):
    print('YES')
elif (a % 2 == 0) and (b % 2 == 1):
    print('YES')
else:
    print('NO')

print(a-b)


print('Gold',input())
print('Silver',input())
print('Bronze',input())

t = input().upper()