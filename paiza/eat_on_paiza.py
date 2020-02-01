M, N = map(int, input().split())

foods = []

for i in range(M):
    food = int(input())
    foods.append(food)

for i in range(N):
    calories = 0
    eat = list(map(int,input().split()))
    for i in range(M):
        calory = foods[i]*eat[i]//100
        print(calory)
    
print(foods)