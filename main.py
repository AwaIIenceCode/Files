#var_1
with open('input.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()
    print(f"Number of characters in a file: {len(content)}")

#var_2
with open('input.txt', 'r', encoding='utf-8') as infile:
    total_characters = 0

    for line in infile:
        total_characters += len(line)

print(f"Total number of characters: {total_characters}")
