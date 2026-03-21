def count_duplicate_words(sentence):

# Split the sentence into words

words = sentence.split()

# Create a dictionary to store word counts

word_count = {}

# Count occurrences of each word

for word in words:

# Convert to lowercase for case-insensitivity

word = word.lower()

if word in word_count:

word_count[word] += 1

else:

word_count[word] = 1

# Find and print duplicate words

duplicates = {word: count for word, count in word_count.items() if count > 1}

if duplicates:

print("Duplicate words and their counts:")
for word, count in duplicates.items():

print(f"{word}: {count}")

else:

print("No duplicate words found.")

# Example usage

sentence = input("Enter a sentence: ")

count_duplicate_words(sentence)
