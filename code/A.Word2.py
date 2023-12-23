def correct_word_case(word):
    uppercase_count = sum(1 for c in word if c.isupper())
    lowercase_count = len(word) - uppercase_count
    
    if uppercase_count > lowercase_count:
        corrected_word = word.upper()
    else:
        corrected_word = word.lower()
    
    return corrected_word

# Read input
word = input().strip()

# Call the function and print the result
corrected_word = correct_word_case(word)
print(corrected_word)
