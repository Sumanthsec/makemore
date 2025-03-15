# Open the file and read words
with open('names.txt', 'r') as file:
    words = [line.strip() for line in file]

# Count words that end with 'm'
count = sum(1 for word in words if word.endswith('m'))

print(f"Number of words ending with 'm': {count}")
