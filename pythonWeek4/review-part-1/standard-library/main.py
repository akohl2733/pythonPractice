from collections import Counter
from bs4 import BeautifulSoup
import requests

countries = ["spain", "france", "argentina", "brazil", "usa", "germany", "netherlands", "hungary", "russia", "japan", "portugal", 'croatia', 'england', 'italy']

url = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"

# response = requests.get(url)
# html_content = response.text

# soup = BeautifulSoup(html_content, "html.parser")
# all_a_tags = soup.find_all("a")

# final_amount = []
# for link in all_a_tags:
#     text = link.get_text().strip().lower()
#     if text in countries:
#         final_amount.append(text)

# print("Final amount per country:", Counter(final_amount))

### --------------------------------------

from itertools import chain, permutations

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

tup3 = list(chain(tup1, tup2))

# print(tup3)

letters = ["a", 'b', 'c', 'd']
letters2 = ["a", 'b', 'c', 'd', 'e', 'f']

perms = list(permutations(letters))
perms2 = list(permutations(letters2))
# print("Length of first:", len(perms))
# print("Length of second:", len(perms2))

### --------------------------------------