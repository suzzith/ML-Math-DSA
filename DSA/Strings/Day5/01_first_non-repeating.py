s = "abbcdde"
freq = {}

# Step 1: Count frequency of each character
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Find first non-repeating character
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
