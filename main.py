with open('input.txt', 'r', encoding='utf-8') as infile:
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line)