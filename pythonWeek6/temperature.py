class Temperature:

    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

    @staticmethod
    def is_valid_temp(value: float) => bool:
        return value >= -273.15

    def __repr__(self):
        return f"{self.celsius:.2f}°C / {self.to_fahrenheit():.2f}°F" 


class LibraryBook:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.availability = True

    def checkout(self):
        if self.availability != True:
            print("Book is already unavailable.")
            return
        self.availability = False
        print(f"{self.title} is now successfully checked out.")

    def is_checked_out(self) -> bool:
        return not self.availability

    @classmethod
    def from_string(cls, book: str):
        title, author = book.split(",")
        return cls(title.strip(), author.strip())

    @staticmethod
    def is_valid_isbn(value: int) -> bool:
        return len(int) == 13 and value.isdigit()

    def __repr__(self):
        return f"Title:{self.title}, Author:{self.author}, Available:{self.availability}"