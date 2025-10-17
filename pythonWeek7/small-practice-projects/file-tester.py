from collections import Counter
import string

words_list = []

with open("testing.txt", 'r') as f:
    text = f.read().lower()
    for punct in string.punctuation:
        text = text.replace(punct, "")
    words_list = text.split()

res = Counter(words_list).most_common(5)
for word, occurences in res:
    print(f"'{word}' -- {occurences}x")