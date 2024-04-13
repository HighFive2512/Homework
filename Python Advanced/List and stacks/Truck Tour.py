from collections import deque

petrol_distance = deque(
    [[int(pump) for pump in input().split()] for _ in range(int(input()))]
)

pump_data = petrol_distance.copy()
petrol_in_tank = 0
iter = 0
while pump_data:
    petrol, dist = pump_data.popleft()

    petrol_in_tank += petrol

    if petrol_in_tank >= dist:
        petrol_in_tank -= dist
    else:
        petrol_distance.rotate(-1)
        pump_data = petrol_distance.copy()
        iter += 1
        petrol_in_tank = 0
print(iter)
