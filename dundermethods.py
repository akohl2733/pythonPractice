class CustomList:

    def __init__(self, data=None):
        self.items = data if data else []

    def __repr__(self):
        return f'CustomList: {self.items}'
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, idx, val):
        self.items[idx] = val
    
    def __eq__(self, obj):
        if isinstance(obj, CustomList):
            return self.items == obj.items
        return False
    
    def __contains__(self, item):
        return item in self.items
    
    def __add__(self, obj):
        if isinstance(obj, CustomList):
            return CustomList(self.items + obj.items)
        raise TypeError("Can only add another CustomList")
    
    def __iter__(self):
        return iter(self.items)
    

# ---------------------------------------------------
# GradeBook project


class GradeBook:

    def __init__(self):
        self.grades = {}

    def __str__(self):
        return "\n".join([f'{student}: {grade}' for student, grade in self.grades.items()])
    
    def __repr__(self):
        return "\n".join([f'(Student Name) = {s} // (Grade) = {g}' for s, g in self.grades.items()])
    
    def __len__(self):
        return len(self.grades)
    
    def __contains__(self, name):
        return name in self.grades.keys()
    
    def __getitem__(self, key):
        return self.grades[key]
    
    def __setitem__(self, key, value):
        self.grades[key] = value

    def __eq__(self, obj):
        if isinstance(obj, GradeBook):
            return self.grades == obj.grades
        return False

    def __add__(self, obj):
        if isinstance(obj, GradeBook):
            combined = GradeBook()
            combined.grades = {**self.grades, **obj.grades}
            return combined
        raise TypeError("Can only add another GradeBook")
    
    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0
    