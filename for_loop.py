hello = "This is a for loop example."
print(hello)

word_to_find = "loop"
found= False

for word in hello.split():
    if word == word_to_find:
        found = True
        print(f'Found the word: "{word_to_find}"')
        break

if not found:
    print(f'Word "{word_to_find}" not found.')