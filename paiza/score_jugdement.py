n = int(input())
arr = []
for i  in range(n):
    arr.append(list(map(str, input().rstrip().split())))

count = 0

for t in range(n):
    if int(arr[t][1])+int(arr[t][2])+int(arr[t][3])+int(arr[t][4])+int(arr[t][5]) >= 350:
        if arr[t][0] == 's':
            if int(arr[t][2])+int(arr[t][3]) >= 160:
                count += 1
        elif arr[t][0] == 'l':
            if int(arr[t][4])+int(arr[t][5]) >= 160:
                count += 1
print(count)