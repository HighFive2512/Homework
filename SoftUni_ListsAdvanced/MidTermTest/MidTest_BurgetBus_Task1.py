ncities = int(input())
totalinc = 0
totalexp = 0
for eachcity in range(1,ncities+1):
    cityname,moneyearnerd,expenses = input(),float(input()),float(input())
    if eachcity % 3 == 0 and eachcity % 5 != 0:
        expenses += expenses*0.5
    if eachcity % 5 == 0:
        moneyearnerd -= moneyearnerd*0.1
    totalexp += expenses
    totalinc += moneyearnerd
    print(f'In {cityname} Burger Bus earned {"{:.2f}".format((moneyearnerd - expenses))} leva.')
profit = totalinc - totalexp
print(f'Burger Bus total profit: {"{:.2f}".format(profit)} leva.')