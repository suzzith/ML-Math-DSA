s = "abbcdde"
freq = {}
res = []

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 2 and ch not in res:
        res.append(ch)

print("Chars with frequency 2:", res)
