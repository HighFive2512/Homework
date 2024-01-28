
total_food_qty = int(input())
orders = input()
orders = [int(i) for i in orders.split(" ")]
highest_order = max(orders)
total_orders = len(orders)

iter = 0
while iter < total_orders:
    if total_food_qty - int(orders[0]) >= 0:
        total_food_qty -= int(orders[0])
        orders.pop(0)
        iter += 1

    else:
        break

print(highest_order)
if len(orders) == 0:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(map(str, orders))}')
