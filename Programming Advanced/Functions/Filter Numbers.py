def even_odd_filter(**num_sets):
    if "odd" in num_sets:
        num_sets["odd"] = [n for n in num_sets["odd"] if n % 2 != 0]
    if "even" in num_sets:
        num_sets["even"] = [n for n in num_sets["even"] if n % 2 == 0]
    return dict(sorted(num_sets.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))