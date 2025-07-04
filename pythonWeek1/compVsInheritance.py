class Publisher:

    def __init__(self, name, city_published):
        self.name = name
        self.city = city_published

    def __str__(self):
        return f"{self.name} ({self.city})"


class Author:

    def __init__(self, name, birth_year, nationality):
        self.name = name
        self.year = birth_year
        self.nation = nationality

    def __str__(self):
        return f'{self.name} ({self.nation}, born {self.year})'
    
    def get_bio(self):
        return f'{self.name} is a {self.nation} author born {self.year}'
    

class Book:

    def __init__(self, title, genre, author, publisher):
        self.title = title
        self.genre = genre
        self.author = author        # Book has an author -- composition
        self.publish = publisher

    def __str__(self):
        return f"'{self.title}' -- {self.genre}\nBy {self.author}"
    
    def summary(self):
        return (
            f"'{self.title} is a {self.genre} book written by {self.author.name}.\n"
            f"It was published in {self.publish.city} by {self.publish.name}"
        )
    

pub = Publisher("Scholastic Press", "New York")
author = Author("JK Rowling", 1950, 'British')
hpdh = Book("Harry Potter: The Deathly Hallows", "Fantasy", author, pub)
print(hpdh.summary())