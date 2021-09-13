class Person:
    """Person class"""

    def __init__(self, name, age):
        """Person constructor"""
        self.name = name
        self.age = age

    def __str__(self):
        """Converting class to string"""
        return f"{self.name}, age: {self.age}"
