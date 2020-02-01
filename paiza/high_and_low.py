M, N = map(int, input().split())

z = int(input())

for i in range(z):
    x, y = map(int, input().split())
    if x > M:
        print('Low')
    elif x == M:
        if y < N:
            print('Low')
        else:
            print('High')
    else:
        print('High')