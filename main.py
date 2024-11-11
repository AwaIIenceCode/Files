with open('file1.txt', 'r', encoding='utf-8') as file1, open('file2.txt', 'r', encoding='utf-8') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

for i in range(min(len(lines1), len(lines2))):
    if lines1[i] != lines2[i]:
        print(f"Line {i + 1} does not match:")
        print(f"File 1: {lines1[i].strip()}")
        print(f"File 2: {lines2[i].strip()}")

if len(lines1) != len(lines2):
    print("\nFiles have a different number of lines.")