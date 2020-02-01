n = int(input())

start = []
end = []
high =[]
low = []
for i in range(n):
    a, b , c , d = map(int, input().split())
    start.append(a)
    end.append(b)
    high.append(c)
    low.append(d)    
    
print(start[0],end[n-1],max(high),min(low))

