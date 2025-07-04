sentence = "hello world hello code code test"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word in words:
    if freq[word]==1:
        print("first uniq word:",word)
        break