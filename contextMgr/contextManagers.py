class FileHandler:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open (self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f"Closed {self.filename}")


# with FileHandler('sample.txt', 'w') as f:
#     f.write("Hello!")

## ----------------------------------------------------

import time

class Timer:

    def __init__(self, label = None):
        self.start_time = 0
        self.end_time = 0
        self.label = label
        
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, x, y, z):
        self.end_time = time.perf_counter()
        print(f"[Timer{f': {self.label}' if self.label else ""}] Block executed in {self.end_time - self.start_time:.4f} seconds.")

with Timer("test"):
    time.sleep(2)


# ---------------------------------------------------------


class SafeFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f'{self.filename} opened')
        return self.file
    
    def __exit__(self, x, y, z):
        self.file.close()
        print(f"{self.filename} closed")