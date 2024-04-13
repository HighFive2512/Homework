products = {}
while True:
    uinput = input()
    if uinput.strip() == "buy":
        break
    uinput = uinput.split(" ")
    productname = uinput[0]
    productprice = uinput[1], uinput[2]
    if productname not in products:
        products[productname] = productprice
    else:
        products[productname] = uinput[1], (
            int(products[productname][1]) + int(uinput[2])
        )
sum_dict = {key: (float(value[0]) * float(value[1])) for key, value in products.items()}
res = [
    print(f'{product_name} -> {"{:.2f}".format(total_price)}')
    for product_name, total_price in sum_dict.items()
]
