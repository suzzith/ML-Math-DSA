s = "hello"
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_list = [ch for ch in s if ch.lower() in vowels]
res = ""

for ch in s:
    if ch.lower() in vowels:
        res += vowel_list.pop()  # Insert reversed vowel
    else:
        res += ch

print("Output:", res)
