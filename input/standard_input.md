# はじめに
競技プログラミングを最近始めたので案外めんどくさい標準入力についてまとめました。
一度にすべてはめんどくさいので徐々に更新していきます。



```:高速化
import sys
input = sys.stdin.readline
```

```:input
apple
orange
10
12.5
```

```
a = input()
b = str(input())
c = int(input())
d = float(input())
```


```
1
2
3
4
5
```

```
X = [int(input()) for i in range(5)]
print(X)
```
```
[1, 2, 3, 4, 5]
```

```:input
1 2 3 4 5
```


```
A = list(map(int,input().split()))
print(A)
```

```:output
[1, 2, 3, 4, 5]
```

まだ処理待ち

list in tuple
```
list = []
n = int(input())
for i in range(n):
    a,b=input().split()
    list.append((int(a), b))
```

list in list(int)

```
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
```

List in list(str)

```
5
-7 -10 U
7 -6 U
-8 7 D
-3 3 D
0 -6 R
```

```
N = int(input()) 
Array = [list(map(str, input().split())) for _ in range(N)]
```
