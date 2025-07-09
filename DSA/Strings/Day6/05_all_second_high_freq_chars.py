def second_most_frequent_chars(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    unique_freqs = sorted(set(freq.values()), reverse=True)

    if len(unique_freqs) < 2:
        print("No second most frequent characters")
        return

    second_highest = unique_freqs[1]

    result = [ch for ch, count in freq.items() if count == second_highest]
    print("Second most frequent characters:", result)

s = "aabbbccdd"
second_most_frequent_chars(s)
