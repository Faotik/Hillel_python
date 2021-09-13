from person import Person

class Teacher(Person):
    """Teacher class"""

    def __init__(self, name, age):
        """Teacher constructor"""
        super().__init__(name, age)
        self.courses = []

    def add_course(self, course):
        """Add course for Teacher"""
        self.courses.append(course)

    def __str__(self):
        """Converting class to string"""
        ret = f"{self.name}, age: {self.age}:\n"
        ret = ret + "\tCourses:\n"
        for c in self.courses:
            ret = ret + "\t\t" + str(c) + "\n"
        return ret
