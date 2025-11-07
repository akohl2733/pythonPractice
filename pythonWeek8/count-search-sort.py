from typing import List

def find_unique_elements(lst: List[any]):

    return set(lst)


def manual_search(lst: List[any], target):

    for k, v in enumerate(lst):
        if v == target:
            return k
    return -1


def binary_search(lst: List[int], target):

    l, r = 0, len(lst) - 1

    while l <= r:
        mid = (1+r)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            l = mid + 1
            mid = (l+r)//2
        else:
            r = mid - 1
    return -1


def check_for_anagrams(lst1, lst2):
    
    seen = {}

    for l in lst1:
        if l in seen:
            seen[l] += 1
        else:
            seen[l] = 1

    for l in lst2:
        if l not in seen:
            return False
        seen[l] -= 1

    return all(v == 0 for v in seen.values())