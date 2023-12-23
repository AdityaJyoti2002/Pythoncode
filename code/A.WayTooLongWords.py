def abbreviate_word(word):
    if len(word) <= 10:
        return word
    else:
        return word[0] + str(len(word) - 2) + word[-1]

# Read the number of words
n = int(input())

# Read and process each word
for _ in range(n):
    word = input().strip()
    abbreviated_word = abbreviate_word(word)
    print(abbreviated_word)
