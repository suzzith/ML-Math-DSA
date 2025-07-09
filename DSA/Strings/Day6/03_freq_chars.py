def freq_char(s):
    freq = {}
    res = []

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] > 1 and ch not in res:
            res.append(ch)

    return res

s = "aabbccddeeffgghhi"
print(freq_char(s))  
