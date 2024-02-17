import re

totalamount = 0

while True:
    user_input = input().strip()

    if user_input == "end of shift":
        print(f'Total income: {"{:.2f}".format(totalamount)}')
        break

    match = re.match(r'%([A-Za-z]+)%[^\|\.\$\%]*?<([A-Za-z]+)>[^\|\.\$\%]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])\$', user_input)

    if match:
        customer, product, count, price = match.groups()
        if 'invalid' in customer.lower() or 'invalid' in product.lower():
            continue

        count, price = int(count), float(price)
        total = count * price
        totalamount += total

        print(f"{customer}: {product} - {'{:.2f}'.format(total)}")