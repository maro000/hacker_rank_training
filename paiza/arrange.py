a ,b ,c = (map(str, input().split()))
def rolling(text, n):
    return text[n:] + text[:n]

count = 0
for i in range(int(a)):
    tx = rolling(c,i)
    if b == tx:
        print(count)
        break
    else:
        count += 1


# https://www.isc.meiji.ac.jp/~mizutani/python/intro3_python.html