search_word = input("Enter the word to count: ")

with open('input.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    count = 0

for word in words:
    if word == search_word:
        count += 1

print(f"The word '{search_word}' appears {count} times.")
