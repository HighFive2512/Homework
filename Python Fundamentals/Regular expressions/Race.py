import re

participants = input().split(",")
res = {x.strip(): 0 for x in participants}
while True:
    racer_distance = 0
    obfuscated_string = input().strip()
    if obfuscated_string == "end of race":
        break
    all_letters = re.findall(r"[A-Za-z]+", obfuscated_string)
    racer_name = "".join(all_letters)
    all_numbers = [int(i) for i in re.findall(r"\d", obfuscated_string)]
    if racer_name in res:
        res[racer_name] += sum(all_numbers)
final_result = sorted(res.items(), key=lambda x: x[1], reverse=True)
print(
    f"1st place: {final_result[0][0]}\n2nd place: {final_result[1][0]}\n3rd place: {final_result[2][0]}"
)
