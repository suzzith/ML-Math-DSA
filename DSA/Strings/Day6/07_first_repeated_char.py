def first_repeated_char(s):
    seen = set()

    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

s = "abca"
print("First repeated character:", first_repeated_char(s))
