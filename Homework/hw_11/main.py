from homework import Homework
from course import Course
from teacher import Teacher
from student import Student
from employee import Employee
from table import Table



students = [
    Student("Student 1", 12, "Python"), Student("Student 2", 16, "Python"), Student(
        "Student 3", 15, "Python"), Student("Student 4", 14, "Python")
]

table = Table()

table.add_students(students)

table.add_homework_for_all_students(Homework("Homework1", "Description1", 2, False))
table.add_homework_for_all_students(Homework("Homework2", "Description2", 3, False))

table.change_homework_status_for_student(2, 0, True)

table.sort_students_by_age()

course1 = Course("Python easy", "Description1", "09.03.21", "09.06.21", 16)
course2 = Course("Python easy-meduim", "Description2", "08.03.21", "08.06.21" "Description1", 16)
course3 = Course("Python medium", "Description3", "07.03.21", "07.06.21", 12)
course4 = Course("Python medium-hard", "Description4", "06.03.21", "06.06.21", 12)
course5 = Course("Python medium-hard", "Description5", "05.03.21", "05.06.21", 11)

courses = [course1, course2, course3, course4, course5]
for course in courses:
    course.add_students(students)

table.add_courses(courses)

teacher = Teacher("Viktor", 23)
teacher2 = Teacher("Nike", 30)
teacher.add_course(table.get_course(0))
teacher.add_course(table.get_course(1))
teacher2.add_course(table.get_course(2))
teacher2.add_course(table.get_course(3))
teacher2.add_course(table.get_course(4))
teachers = [teacher, teacher2]

employee = Employee("Mike", 23, 1000)

table.add_teachers(teachers)
table.add_employee(employee)

print("..............................\n")
print(table)
print("\n..............................\n")

input()
