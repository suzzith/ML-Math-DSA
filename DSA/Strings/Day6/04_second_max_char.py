def second_max_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Convert frequencies to a list of (char, freq) tuples and sort
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_freq) >= 2:
        print("Second most frequent char:", sorted_freq[1][0])
    else:
        print("No second most frequent char")

s = "aaabbc"
second_max_char(s)
