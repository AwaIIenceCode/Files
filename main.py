lines = ["Row 1", "Row 2", "Row 3"]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in lines:
        outfile.write(line + '\n')