from collections import deque
from datetime import datetime,timedelta


robos = {}
products = deque()

for each_robot in input().split(";"):
    name,req_time = each_robot.split("-")
    robos[name] = [int(req_time),0]

processing_time = datetime.strptime(input(),'%H:%M:%S')

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    processing_time += timedelta(seconds=1)
    product = products.popleft()

    available_robots = []

    for rob_name, val in robos.items():
        if val[1] != 0:
            robos[rob_name][1] -= 1
        if val[1] == 0:
            available_robots.append([rob_name,val])

    if not available_robots:
        products.append(product)
        continue

    robos_name, info = available_robots[0]
    robos[robos_name][1] = info[0]

    print(f'{robos_name} - {product} [{processing_time.strftime("%H:%M:%S")}] ')