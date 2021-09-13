class Course:
    """Course class"""

    def __init__(self, name, description, date_of_start_course, date_of_end_course, lessonCount):
        """Course constructor"""
        self.name = name
        self.description = description
        self.students = []
        self.date_of_start_course = date_of_start_course
        self.date_of_end_course = date_of_end_course
        self.lessonCount = lessonCount

    def __str__(self):
        """Converting class to string"""
        ret = ""
        ret += f"{self.name}, {self.description}, {self.date_of_start_course}, {self.date_of_end_course}, {self.lessonCount} \n"
        ret += "\t\tStudents:\n"
        for student in self.students:
            ret += f"\t\t\t{student.name}\n"
        return ret

    def add_student(self, student):
        """Add student to course"""
        self.students.append(student)

    def add_students(self, students):
        """Add students to course"""
        for student in students:
            self.students.append(student)
