s = "aabbcdde"
freq = {}

# Step 1: Count frequencies
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Find first repeating
for ch in s:
    if freq[ch] > 1:
        print(ch)
        break
