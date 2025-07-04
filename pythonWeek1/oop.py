
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
        
        
class Dog(Animal):

    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def speak(self):
        return "Woof"
    
    def getAge(self):
        return self.age
    
dog1 = Dog("Zeke", 'aussie', 10)
dog2 = Dog('Oliver', "maltese", 14)

# print(dog1.name, dog2.breed, dog2.age)
# print(dog1.bark())

class Cat(Animal):

    def __init__(self, name, color, is_indoor):
        super().__init__(name)
        self.color = color
        self.is_indoor = is_indoor
    
    def speak(self):
        return "Meow"
    
    def describe(self):
        if self.is_indoor:
            pref = "indoor"
        else:
            pref = "outdoor"
        return f'This cat\'s name is {self.name} and they are {self.color}.\nThis is an {pref} cat.'

objs = [Dog("Zeke", "Aussie", 9), Cat("Lu", "Grey", True)]
for obj in objs:
    print(obj.speak())


# Task B: Cat class
# Attributes: name, color, is_indoor

# Methods: meow(), describe()

# Example Skeleton:
# python
# Copy
# Edit
# class Cat:
#     def __init__(self, name, color, is_indoor):
#         self.name = name
#         self.color = color
#         self.is_indoor = is_indoor

#     def meow(self):
#         return f"{self.name} says meow!"

#     def describe(self):
#         return f"{self.name} is a {self.color} cat. Indoor: {self.is_indoor}"
# 5. 🧪 Practice Prompt:
# Write a small script that:

# Creates a list of Dog and Cat objects

# Loops through them

# Calls a method like .bark() or .meow() based on the type