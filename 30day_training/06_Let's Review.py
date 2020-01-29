# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
# print(n)

for i in range(n):
    S = input()
    
    for j in range(len(S)):
        if j % 2 == 0:
            print(S[j],end='')
    
    print(' ', end ='')

    for j in range(len(S)):
        if j % 2 == 1:
            print(S[j],end='')
            
    print('')