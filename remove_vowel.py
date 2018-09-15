def disemvowel(word):
    l_word = list(word)
    dis_word = [item.strip("aAiIuUeEoO") for item in l_word]
    dis_word = "".join(dis_word)
    return dis_word
