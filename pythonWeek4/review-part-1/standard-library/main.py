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

import requests
import sys 

def fetch_posts(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)

        print(f"\n📰 Post ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    
    except requests.exceptions.HTTPError:
        print(f"Error: Post ID {post_id} not found.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <post_id>")
        return

    post_id = sys.argv[1]
    fetch_posts(post_id)

if __name__ == "__main__":
    main()