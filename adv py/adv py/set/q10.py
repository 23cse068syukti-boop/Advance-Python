numbers = [1, 2, 3, 2, 4, 5, 1]

seen = set()
repeated = set()

for num in numbers:
    if num in seen:
        repeated.add(num)
    else:
        seen.add(num)

print(repeated)
