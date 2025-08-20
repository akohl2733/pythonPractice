class Person:

    species = "Home sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)

    def __repr__(self):
        return f"Name:{self.name}\nAge:{self.age}"

print(Person.get_species())

person_from_year = Person.from_birth_year("Andrew", 2000)
print(person_from_year.name)
print(repr(person_from_year))