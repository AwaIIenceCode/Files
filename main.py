with open("input.txt", "r", encoding="utf-8") as file:
    words = file.read().split()
    count_words = 0

long_words = []
for word in words:
    if len(word) >= 7:
        long_words.append(word)
        count_words += 1

print("Words at least 7 characters long:\n")
print(long_words)
print(f"\nNumber of such words: {count_words}")

with open("output.txt", "w", encoding="utf-8") as output_file:
    for word in long_words:
        output_file.write(word + "\n")
