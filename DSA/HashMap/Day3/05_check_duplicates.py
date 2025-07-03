def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            print("Duplicate found:", num)
            return True
        seen.add(num)
    print("No duplicates")
    return False

# Test
has_duplicates([1, 2, 3, 4, 5, 2])
has_duplicates([1, 2, 3])
