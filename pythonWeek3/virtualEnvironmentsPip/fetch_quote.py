import requests

def get_quote():    
    quote = requests.get("https://api.quotable.io/random", verify=False)
    if quote.status_code == 200:
        res = quote.json()
        print(f'{res['content']} - {res['author']}')
    else:
        print("Was not able to get quote.")


if __name__ == "__main__":
    get_quote()