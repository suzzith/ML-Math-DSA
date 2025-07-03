def is_anagram(a, b):
    if len(a) != len(b):
        return False

    freq1 = {}
    freq2 = {}

    for ch in a:
        freq1[ch] = freq1.get(ch, 0) + 1
    for ch in b:
        freq2[ch] = freq2.get(ch, 0) + 1

    return freq1 == freq2

# Test
print("anagrams" if is_anagram("listen", "silent") else "not anagram")
