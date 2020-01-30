import collections

for i in range(int(input())):
    num = input()
    l_num = list(num)
    l_num = [s for s in l_num]
    c = collections.Counter(l_num)
    if (c.most_common()[0][1]) == 4:
        print('Four Card')
    elif (c.most_common()[0][1]) == 3:
        print('Three Card')
    elif (c.most_common()[0][1]) == 2:
        if (c.most_common()[1][1]) == 2:
            print('Two Pair')
        if (c.most_common()[1][1]) == 1:
            print('One Pair')
    else:
        print('No Pair')

# https://note.nkmk.me/python-collections-counter/