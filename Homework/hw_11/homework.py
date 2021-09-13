class Homework:
    """Homework class"""

    def __init__(self, name, description, complexity, status):
        """Homework constructor"""
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status
        self.grade = 0

    def __str__(self):
        """Converting class to string"""
        return f"{self.name}, {self.description}, {self.complexity}, {self.status}"

    def change_status(self, status):
        """Change status for homework"""
        self.status = status
