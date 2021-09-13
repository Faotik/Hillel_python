from person import Person

class Employee(Person):
    """Employee class"""

    def __init__(self, name, age, salary = 0):
        """Employee constructor"""
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        """Converting class to string"""
        return f"{self.name}, age: {self.age}, salary: {self.salary}"

    def change_salary(self, salary):
        """Change employee salary"""
        self.salary = salary
