import time
import threading

def download_file(name, seconds):
    print(f"Starting {name}")
    time.sleep(seconds)
    print(f"Finished {name}")

def sequential():
    start = time.time()
    download_file("File1", 2)
    download_file("File2", 2)
    download_file("File3", 2)
    print(f"Sequential took {time.time() - start:.2f} seconds")

def threaded():
    start = time.time()
    threads = [
        threading.Thread(target=download_file, args=(f"File{i}", 2))
        for i in range(1, 4)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Threaded took {time.time() - start:.2f} seconds")

sequential()
threaded()