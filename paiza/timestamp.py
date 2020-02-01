t = str(input())

date = int(t[3:5])
if int(t[6:8]) >= 24:
    cnt = int(t[6:8])//24
    cal = int(t[6:8]) - 24*cnt
    hour ='0'+str(cal)
    # print(hour)
    # print(cnt)
    date += cnt
    print(t[:3]+str(date),str(hour)+t[-3:])
else:
    print(t)
    
# print(date)
