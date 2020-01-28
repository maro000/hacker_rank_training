# 高速化
import sys
input = sys.stdin.readline


a = input()
b = str(input())
c = int(input())
d = float(input())

N = int(input())
A = list(map(int,input().split()))

print(N) # 入力:3 出力:3
print(A) # 入力:1 3 2 出力:[1, 3, 2]

x, y = map(int, input().split())           # 入力:1 2
a, b = map(int, input().split(','))        # 入力:1, 2
c, d, e = map(str, input().split())        # 入力:1 2 3
A = [int(i) for i in input().split()]      # 入力:1 2 3 4 5 6
B = list(str(i) for i in input().split())  # 入力:1 2 3 4 5 6
C = list(map(int, input().split()))        # 入力:1 2 3 4 5 6

print(x,y)                                 # 1 2
print(a,b)                                 # 1 2
print(c, d, e)                             # 1 2 3
print(A)                                   # [1, 2, 3, 4, 5, 6]
print(B)                                   # [1, 2, 3, 4, 5, 6]
print(C)                                   # [1, 2, 3, 4, 5, 6]

X = [int(input()) for i in range(5)]
# 入力: 
# 1
# 2
# 3
# 4
# 5
print(X) # [1, 2, 3, 4, 5]

N = int(input()) # 入力: 5
Array = [list(map(str, input().split())) for _ in range(N)]
# 入力:
# -7 -10 U
# 7 -6 U
# -8 7 D
# -3 3 D
# 0 -6 R
print(Array) # [['-7', '-10', 'U'], ['7', '-6', 'U'], ['-8', '7', 'D'], ['-3', '3', 'D'], ['0', '-6', 'R']]

list = []
for i in range(5):
    a,b=input().split()
    list.append((int(a), b))