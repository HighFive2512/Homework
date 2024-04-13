def age_assignment(*names, **age_data):
    result = []

    for let, age in age_data.items():
        for n in names:
            if n.startswith(let):
                result.append(f"{n} is {age} years old.")
                break

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
