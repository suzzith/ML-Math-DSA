def remove_chars(s1, s2):
    block = set(s2)  # store all chars from s2 in a set for fast lookup
    result = ""

    for ch in s1:
        if ch not in block:
            result += ch

    return result

s1 = "battle"
s2 = "bat"
print("Result:", remove_chars(s1, s2))
