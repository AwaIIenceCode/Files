with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in reversed(lines):
        outfile.write(line)
