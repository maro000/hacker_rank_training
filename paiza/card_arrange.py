a = list(map(int, input().rstrip().split()))
a.sort()

x = int(str(a[-1])+str(a[-3]))
y = int(str(a[-2])+str(a[-4]))
sum =  x + y
print(sum)

