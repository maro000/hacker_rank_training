R = list(map(str, input().rstrip().split(' ')))

if R[0] == 'x':
    if R[1] == '+':
        print(abs(int(R[4]) - int(R[2])))
    else:
        print(abs(int(R[4]) + int(R[2])))
elif R[2] == 'x':
    if R[1] == '-':
        print(abs(int(R[4]) - int(R[0])))
    else:
        print(abs(int(R[4]) + int(R[0])))
elif R[4] == 'x':
    if R[1] == '+':
        print(abs(int(R[0]) + int(R[2])))
    else:
        print(abs(int(R[0]) - int(R[2])))

