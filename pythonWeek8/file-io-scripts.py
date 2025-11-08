file = "sample.txt"

def find_common_word(file, word: str):
    with open(file, 'r') as f:
        lines = [l.strip().lower() for l in f.readlines()]
        count = 0
        for line in lines:
            if word.strip().lower() in line:
                count += 1
        return count
    

data = ["1,2,3,4,5\n", "6,7,8,9,10\n", "11,12,13,14,15\n"]

def add_filtered_date(file, data):
    with open(file, "w") as f:
        f.writelines(data)
        return
add_filtered_date("new.txt", data)