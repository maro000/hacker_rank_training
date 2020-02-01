x, p = map(int, input().split())

pay = 0
while x > 0:
    pay += x
    x = (x * (100-p) //100)
print(pay)