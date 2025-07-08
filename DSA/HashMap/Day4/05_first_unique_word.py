def uniq_word(s):
    words = s.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    for word in words:
        if freq[word] == 1:
            return word

    return -1

s = "Hi there hi Hello"
print("First unique word:", uniq_word(s))
