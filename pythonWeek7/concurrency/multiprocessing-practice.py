from multiprocessing import Process
import time

def compute(n):
    print(f"Computing {n}...")
    total = sum(i*i for i in range(10_000_000))
    print(f"Done with {n}")
    return total

def run():
    start = time.time()
    processes = [Process(target=compute, args=(i,)) for i in range(1, 4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Multiprocessing took {time.time() - start:.2f} seconds")

run()