sentence = "python is easy and python is powerful"

words = sentence.split()
unique_words = set(words)

result = " ".join(unique_words)
print(result)
