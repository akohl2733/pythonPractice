with open("reminder.txt", "w") as f:
    f.write("Don't forget to breathe and stretch today.\n")

with open("reminder.txt", "r") as f:
    content = f.read()
    print("file says:", content)


with open("log.txt", "a") as f:
    f.write("Log entry: Task Completed!")

with open("log.txt", "r") as f:
    lines = f.readlines()
    print("All log entries.")
    for line in lines:
        print(line.strip())