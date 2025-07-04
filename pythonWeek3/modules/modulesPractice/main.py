from text_operations.cleaner import remove_punctuation
from text_operations.counter import word_count

sample = "I am moving. I went for a walk!"
cleaned = remove_punctuation(sample)
amount_words = word_count(cleaned)

print(f"Cleaned: {cleaned}")
print(f"Words: {amount_words}")