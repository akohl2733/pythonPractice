def remove_punctuation(text):
    return ''.join(t for t in text if t.isalnum() or t.isspace())