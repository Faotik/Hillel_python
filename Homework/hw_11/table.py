from homework import Homework

class Table:
    """Table class"""

    def __init__(self):
        """Table constructor"""
        self.students = []
        self.teachers = []
        self.employees = []
        self.courses = []

    def __str__(self):
        """Converting class to string"""
        ret = "Students: \n"
        for student in self.students:
            ret += f"\t{student} \n"
        ret += "Teachers: \n"
        for teacher in self.teachers:
            ret += f"\t{teacher} \n"
        ret += "Employees: \n"
        for employee in self.employees:
            ret += f"\t{employee} \n"
        return ret
    def add_student(self, student):
        self.students.append(student)

    def add_students(self, students):
        for student in students:
            self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_teachers(self, teachers):
        for teacher in teachers:
            self.teachers.append(teacher)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_employees(self, employees):
        for employee in employees:
            self.employees.append(employee)
    
    def add_course(self, course):
        self.courses.append(course)

    def add_courses(self, courses):
        for course in courses:
            self.courses.append(course)
    def get_course(self, index):
        try:
            return self.courses[index]
        except:
            return []
    def sort_students_by_age(self):
        self.students = sorted(self.students, key=lambda s: s.age)

    def sort_students_by_grade(self):
        self.students = sorted(self.students, key=lambda s: s.grade)

    def add_homework_for_all_students(self, homework):
        for s in self.students:
            s.add_homework(Homework(homework.name, homework.description, homework.complexity, homework.status))

    def change_homework_status_for_student(self, student_index, homework_index, status):
        self.students[student_index].homeworks[homework_index].change_status(status)
