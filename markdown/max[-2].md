競技プログラミングとかで割と使うので備忘録程度に。

## 2パターンあります

### 1.ソートした後参照するやり方(重複を含む)
Input

```
numbers = [9,2,5,4,7]
a = numbers.sort()
print(a)
```

Output

```
[2,4,5,7,9]
```

Input

```
print(a[-2])
```

Output

```
7
```

### 2.set関数を使ってユニークにしたあとソートして参照する方法(重複を含まない。)

Input

```
nums = [8, 8, 1, 4, 3]
a = set(nums).sort(0)
```

Output

```
{1 ,3 ,4 ,8 }
```

Input

```
print(a[-2])
```

Output

```
4
```