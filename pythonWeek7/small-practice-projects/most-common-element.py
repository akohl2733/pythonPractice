from collections import Counter
from typing import List, Any

def most_common_element(l: List[Any]):

    res = Counter(l).most_common(1)
    return f'Most common element: {res[0][0]}\nOccurences: {res[0][1]}' if res else "No list inputted"

examples = [1, "tree", 'opossum', False, 4, "monkey", "Tree", 1]
empty_list = []

if __name__ == "__main__":
    print(most_common_element(examples))