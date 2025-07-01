import requests

def get_joke():
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if res.status_code == 200:
        print(res.json()["joke"])
    else:
        print("Failed to get joke")

if __name__ == "__main__":
    get_joke()