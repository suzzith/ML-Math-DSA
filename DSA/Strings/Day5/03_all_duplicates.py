s = "abbcdde"
freq = {}
res = []

# Step 1: Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Check duplicates (only once when count == 2)
for ch in s:
    if freq[ch] > 1 and ch not in res:
        res.append(ch)

print("Duplicates:", res)
