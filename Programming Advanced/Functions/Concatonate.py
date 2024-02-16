def concatenate(*words, **kw_words):
    txt = ''.join(words)

    for k, v in kw_words.items():
        txt = txt.replace(k, v)

    return txt
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))