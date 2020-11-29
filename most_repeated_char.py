# Find the most repeated character in a sentence
sentence = "This is a common interview question"

# 1era forma
max_count = 0
for s in sentence:
    count = sentence.count(s)
    if count > max_count:
        max_count = count
        max_char = s
print(f' the most repeated character is {max_char} with a count of {max_count}')

# 2da forma

char_frequency = {}
for s in sentence:
    if s in char_frequency:
        char_frequency[s] += 1
    else:
        char_frequency[s] = 1

print(char_frequency)
char_frequency_sorted = sorted(char_frequency.items(), key=lambda items: items[1], reverse=True)
print(char_frequency_sorted)
print(char_frequency_sorted[0])


