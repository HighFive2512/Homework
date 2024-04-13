from collections import deque

henry_pocket = deque(int(x) for x in input().split())
prices_of_foods = deque(int(x) for x in input().split())
food_eaten = 0


while len(henry_pocket) != 0 and len(prices_of_foods) != 0:
    current_amount, product_price = henry_pocket[-1], prices_of_foods[0]
    if current_amount == product_price:
        henry_pocket.pop()
        prices_of_foods.popleft()
        food_eaten += 1
    elif current_amount < product_price:
        henry_pocket.pop()
        prices_of_foods.popleft()
    else:
        price_difference = current_amount - product_price
        henry_pocket.pop()
        prices_of_foods.popleft()
        if henry_pocket:
            henry_pocket[-1] += price_difference
        food_eaten += 1

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten >= 1:
    if food_eaten == 1:
        print(f"Henry ate: {food_eaten} food.")
    else:
        print(f"Henry ate: {food_eaten} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")
