device_models = [asd for asd in input().split(", ")]

while True:
    kevin_query = input()

    if kevin_query == "End":
        print(*device_models, sep=", ")
        break

    command, device = kevin_query.split(" - ")
    if command == "Add":
        if not device in device_models:
            device_models.append(device)
    if command == "Remove":
        if device in device_models:
            device_models.remove(device)
    if command == "Bonus phone":
        if device.split(":")[0] in device_models:
            position = device_models.index(device.split(":")[0])
            device_models.insert(position + 1, device.split(":")[1])
    if command == "Last":
        if device in device_models:
            device_models.remove(device)
            device_models.append(device)
