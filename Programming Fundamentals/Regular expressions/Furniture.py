import re

products = []
totalamount = 0
while True:
    tempo = ""
    uinput = input()
    if uinput == "Purchase":
        break
    matched_res = re.search(r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)',uinput)
    if matched_res:
        product,price,quantity = matched_res.groups()
        products.append(product)
        totalamount += float(price) * int(quantity)
print("Bought furniture:")
for prdts in products:
    print(prdts)
print(f'Total money spend: {totalamount:.2f}')


