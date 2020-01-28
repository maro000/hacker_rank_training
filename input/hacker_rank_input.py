s1 = input() #文字列で取得し、
print(s1) #文字列のまま出力

s1 = input().strip() #strip()で前後の空白を取り除く

i1 = int(input()) #文字列で取得し、int()に入れ整数として扱う

#入力：str1 str2

s = input().split() #str1 str2をsplit()で分割して取得し、sに値を入れる、split(','),split('/')はぞれぞれ,/で複数要素を分割
print(s) #出力：['str1', 'str2']
print(s[0]) #出力：str1
print(s[1]) #出力：str2

#入力：int1 int2

i = list(map(int, input().split())) #int1 int2を取得し、iに値を入れる。イテレータをlist化している。
print(i[0]) #出力：int1
print(i[1]) #出力：int2

#入力：
# str1
# str2
# str3

s = [input() for i in range(3)] #繰り返し
print(s) #出力['str1', 'str2', 'str3']

#入力：
# N
# str1
# str2
# str3
# .
# . 
# .
# strN

N = int(input()) #1行目のNを取得する
s = [input() for i in range(N)] #N回input()を繰り返す
print(s) #出力：['str1', 'str2', 'str3', 'strN']

N, M = map(int, input().split())
P = [input().split() for i in range(M)]
print(type(P), P)
# <class 'list'> [['1', '32'], ['2', '63'], ['1', '12']]

N, M = map(int,input().split()) 
P = [list(map(int,input().split())) for i in range(M)]
print(type(P), P)
#<class 'list'> [[1, 32], [2, 63], [1, 12]]