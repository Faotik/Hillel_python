from person import Person

class Student(Person):
    """Student class"""

    def __init__(self, name, age, subscribed_course):
        """Student constructor"""
        super().__init__(name, age)
        self.grade = 0
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def __str__(self):
        """Converting class to string"""
        ret = f"{self.name}, age: {self.age}, grade: {self.grade}, course: {self.subscribed_course}:\n"
        ret = ret + "\tHomeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t\t" + str(h) + "\n"
        return ret

    def add_homework(self, homework):
        """Add homework for student"""
        self.homeworks.append(homework)

    def change_homework_status(self, homework_index, status):
        """Change homework status"""
        self.homeworks[homework_index].change_status(status)
