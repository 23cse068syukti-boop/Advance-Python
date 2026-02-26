set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = True

for i in set1:
    if i not in set2:
        is_subset = False
        break

print(is_subset)
