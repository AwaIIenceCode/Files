with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

num_chars = 0
for char in content:
    num_chars += 1

num_lines = 1
for char in content:
    if char == '\n':
        num_lines += 1

num_vowels = 0
for char in content.lower():
    if char in 'aeiou':
        num_vowels += 1

num_consonants = 0
for char in content.lower():
    if char.isalpha() and char not in 'aeiou':
        num_consonants += 1

num_digits = 0
for char in content:
    if char.isdigit():
        num_digits += 1

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f"Number of characters: {num_chars}\n")
    outfile.write(f"Number of lines: {num_lines}\n")
    outfile.write(f"Number of vowels: {num_vowels}\n")
    outfile.write(f"Number of consonants: {num_consonants}\n")
    outfile.write(f"Number of digits: {num_digits}\n")