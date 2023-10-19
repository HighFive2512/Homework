def secret_message(words):
    result = []
    flag = "y"
    for eacword in words.split(" "):
        word_list = [x for x in eacword]
        chrconv = " "
        i = 0
        while i < len(word_list):
            eachchar = word_list[i]
            if eachchar.isnumeric():
                chrconv = str(chrconv) + str(eachchar)
                word_list.pop(i)
                flag = "y"
            if not eachchar.isnumeric() and flag == "y":
                chrconv = int(chrconv)
                word_list.insert(0, chr(chrconv))
                flag = "n"
                word_list[1],word_list[-1] = word_list[-1],word_list[1]
                i += 1
            elif flag == "n":
                i += 1
        result.append(word_list)

    return result


wordstriung = input()
res = secret_message(wordstriung)
res = ' '.join([''.join(word) for word in res])
print(res)