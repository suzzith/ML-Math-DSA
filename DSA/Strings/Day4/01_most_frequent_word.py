sentence = "hello sujith hello satish"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1


most_common = max(freq, key=freq.get)
print("Most frequent word:", most_common)
print("Frequency:", freq[most_common])