from typing import List


def reverse_string(s: str) -> str:
    res = ""
    for char in s[::-1]:
        res += char
    return res


def count_vowels(s: str) -> int:
    vowels = {'a', 'i', 'e', 'o', 'u'}
    counter = 0
    for l in s:
        if l in vowels:
            counter += 1

    return counter


def remove_dupes(l: List[any]) -> List[any]:
    seen = set()
    res = []

    for v in l:
        if v not in seen:
            res.append(v)
            seen.add(v)
    
    return res


def find_max(s: List[int]):
    if len(s) < 1:
        return []
    curr_max = float('-inf')

    for v in s:
        if v > curr_max:
            curr_max = v
    
    return curr_max


def valid_palindrome(s: str):
    s = "".join(c.lower() for c in s if c.isalpha())
    return s == s[::-1]


def find_common_elements(s1, s2):

    seen = {}

    for s in s1:
        seen[s] = 0
    
    for s in s2:
        if s in seen:
            seen[s] = 1
    
    res = []
    for k, v in seen.items():
        if v == 1:
            res.append(k)

    return res


def slice_list(l: List[any], position: int):

    prev = l[:position+1]
    end = l[position+1:]

    end.extend(prev)

    return end


def flatten_list(lst):
    res = []
    for item in lst:
        if isinstance(item, list):
            res.extend(flatten_list(item))
        else:
            res.append(item)
    return res