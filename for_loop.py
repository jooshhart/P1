sentence = "this is a for loop example and this loop is simple"
word_counts = {}

for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:")
for word, count in word_counts.items():
    print(f'"{word}": {count}')