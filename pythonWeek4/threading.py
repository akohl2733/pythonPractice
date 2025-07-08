import threading

def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")

def print_letters():
    for c in "abcde":
        print(f"Thread 2: {c}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Done!")


## ----------------------------------------

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

# print("Final counter", counter)

# -----------------------------------


import requests

image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/320px-June_odd-eyed-cat.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/320px-Cat03.jpg",
]


def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}:", e)

threads = []

for i, url in enumerate(image_urls):
    filename = f"image_{i}.png"
    thread = threading.Thread(target=download_image, args=(url, filename))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("finished")