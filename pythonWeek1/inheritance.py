class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f'Name: {self.name}\nID: {self.id}\nSalary: {self.salary}'
    
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f'Raise: ${amount}\nNew Salary: {self.salary}')
        else:
            print("Please enter a valid, non-negative raise")

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    

class Manager(Employee):

    def __init__(self, name, emp_id, salary, team=None):
        super().__init__(name, emp_id, salary)
        self.team = team if team else []

    def get_details(self):
        emp_details = super().get_details()
        return f'{emp_details}\nEmployees managed: {len(self.team)}'
    
    def add_to_team(self, employee):
        self.team.append(employee)

    def get_team(self):
        if not self.team:
            print("This manager does not have anyone on their team.")
        else:
            print(f"\nTeam member managed by {self.name}:")
            for member in self.team:
                print(member.get_details())

    def give_team_raise(self, amount):
        for member in self.team:
            member.give_raise(amount)

emp1 = Employee("Andrew", 101, 50000)
emp2 = Employee("Zeke", 102, 55000)
emp3 = Employee("Aidan", 103, 60000)
mgr1 = Manager("Chloe", 104, 100000, [emp1, emp2, emp3])

team = [emp1, emp2, emp3, mgr1]
for mem in team:
    print(mem)
    if isinstance(mem, Manager):
        print(mem.get_team())