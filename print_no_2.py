if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

a = []
for i in range(n):
    s = arr[i]
    a.append(s)

t = sorted(set(a))[-2]

print(t)