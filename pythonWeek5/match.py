def favorite_color(color: str) -> str:
    c = color.lower()
    match c:
        case 'red':
            return "You like the devil"
        case 'blue':
            return "You like the ocean"
        case "green":
            return "You like grass"
        case "yellow":
            return "You like the sun"
        case _:
            return "I don't care"

# print(favorite_color("green"))
# print(favorite_color("red"))
# print(favorite_color("yellow"))


class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y 

points = []
points.append(Point(0, 1))
points.append(Point(5, 0))

match points:
    case []:
        print("No Points")
    case [Point(0, 0)]:
        print("The origin")
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")