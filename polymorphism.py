class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())
animal_sound(Cat())


# --------------------------


class Document:

    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __str__(self):
        return f"{self.title}\n{self.content}"
    
    def __len__(self):
        word_list = self.content.split()
        return len(word_list)
    
    def __eq__(self, doc):
        if not isinstance(doc, Document):
            return False
        return self.title == doc.title and self.content == doc.content
    
    def __contains__(self, word):
        return word in self.content

class Book(Document):

    def __init__(self, title, content, author, genre):
        super().__init__(title, content)
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\n{self.content}"
    

class Article(Document):

    def __init__(self, title, content, source, date):
        super().__init__(title, content)
        self.source = source
        self.date = date

    def __str__(self):
        return f"Title: {self.title}\nSource: {self.source}\nDate: {self.date}\n{self.content}"    

class Tweet(Document):

    def __init__(self, title, content, handle):
        if len(content) > 280:
            raise ValueError(f"Content length must not exceed 280 characters")
        
        super().__init__(title, content)
        self.handle = handle

    def __str__(self):
        return f"Title: {self.title}\nHandle: {self.handle}\n{self.content}"