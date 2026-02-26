str1 = "hello"
str2 = "world"

common = set(str1) & set(str2)

new_str1 = "".join([c for c in str1 if c not in common])
new_str2 = "".join([c for c in str2 if c not in common])

print(new_str1)
print(new_str2)
