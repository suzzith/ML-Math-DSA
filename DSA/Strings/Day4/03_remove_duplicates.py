s = "programming"
seen = set()
res = []

for ch in s:
    if ch not in seen:
        seen.add(ch)
        res.append(ch)

print("Without duplicates:", ''.join(res))
