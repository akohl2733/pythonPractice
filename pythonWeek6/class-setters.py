class Rectangle:

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    @property
    def area(self) -> float:
        return self.width * self.length
    
    @area.setter
    def area(self, new_area: float):
        if self.width <= 0:
            raise ValueError("Width must be nonzero to set area.")
        self.length = new_area / self.width