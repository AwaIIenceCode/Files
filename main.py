with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    max_length = 0

for line in lines:
    line = line.strip()
    line_length = len(line)

    if line_length > max_length:
        max_length = line_length

print(f"The length of the longest line is: {max_length}")
