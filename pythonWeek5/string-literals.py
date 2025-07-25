import math

pi = f"The rounded value of pi is {math.pi:.2f}"

things = {"Andrew": 4567, "Kohl": 9876, "Ron": 3623}

for name, phone in things.items():
    print(f"{name:6}  ===>  {phone:4d}")


print("This {food} is {adjective}".format(food="spam", adjective="terrible"))