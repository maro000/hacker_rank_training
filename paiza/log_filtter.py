n = int(input())
arr = list(map(str, input().split()))

x = 'ai'

for i in range(n):
    if "ai" in arr:
        print([arr[i]])