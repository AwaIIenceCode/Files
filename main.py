with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines[:-1])
