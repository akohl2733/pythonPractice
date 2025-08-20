class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Cannot be a negative value")
        self._radius = val
    
    @property
    def area(self):
        return 3.1415927 * (self._radius ** 2)

my_circle = Circle(5)
print(f'Radius is {my_circle.radius}')
print(f'Area is {my_circle.area}')

my_circle.radius = 7
print(f'Radius is {my_circle.radius}')
print(f'Area is {my_circle.area}')