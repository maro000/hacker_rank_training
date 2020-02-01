n = int(input())

def count_diff(a,b):
    cnt = 0
    for c1,c2 in zip(a, b):
        if c1 != c2:
            cnt += 1
    return cnt

score = 0
for i in range(n):
    cor,ans  = map(str,input().split()) 
    if cor == ans:
        score += 2
    elif len(cor) == len(ans):
        if count_diff(cor,ans) == 1:
            score +=1
    

print(score)