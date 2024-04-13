from collections import deque

words = deque(input().split())  # d yel blu e low redd

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

res = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""

    for colour in (first_word + second_word, second_word + first_word):
        if colour in colors:
            res.append(colour)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):  # 'd' 'redd' -> '', 'red'
            if el:
                words.insert(len(words) // 2, el)

for colour in set(req_colors.keys()).intersection(res):
    if not req_colors[colour].issubset(res):
        res.remove(colour)

print(res)
