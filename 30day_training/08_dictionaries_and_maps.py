n = int(input())

l = {}
for i in range(n):
    a , b =  map(str, input().split())
    name = a
    phone = int(b) 
    l[name] = phone


for j in range(n):
  name =input()
  if name in l:
    phone = l[name]
    print(name + '=' + str(phone))
  else:
    print('Not found')


# 下じゃ無いとなぜか通らない

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break