with open('input.txt', 'r', encoding='utf-8') as infile:
    content = infile.read().replace('*', 'TEMP').replace('&', '*').replace('TEMP', '&')

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(content)
