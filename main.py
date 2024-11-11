symbol = input("Enter the latter: ").lower()
count = 0

with open('input.txt', 'r', encoding='utf-8') as infile:
    words = infile.read().split()

    for word in words:
        if word.lower().startswith(symbol):
            count += 1

print(f"The number of words that begin with: '{symbol}': {count}")
