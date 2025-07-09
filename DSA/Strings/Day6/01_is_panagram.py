def is_pangram(s):
    s = s.lower()
    seen = set()

    for ch in s:
        if ch.isalpha():
            seen.add(ch)
    
    if len(seen) == 26:
        print("Pangram")
    else:
        print("Not Pangram")

s = "The quick brown fox jumps over the lazy dog"
is_pangram(s)
