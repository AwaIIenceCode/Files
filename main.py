with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

inserted = False
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in lines:
        outfile.write(line)
        if ',' not in line and not inserted:
            outfile.write('************\n')
            inserted = True

if not inserted:
    with open('output.txt', 'a', encoding='utf-8') as outfile:
        outfile.write('************\n')
