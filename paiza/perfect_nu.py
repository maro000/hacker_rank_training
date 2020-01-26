n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
    
# for i in range(n):
#     arr[i] 
for c in range(n):
    s = 0
    for i in range(1,int(arr[c])):
        if (int(arr[c])) % i == 0:
            s = s + i
    if arr[c] == s:
        print('perfect')
    elif abs(arr[c]-s) == 1:
        print('nearly')
    else:
        print('neither')