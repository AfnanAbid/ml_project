class Student:
    def __init__(self, name, age, python_marks, numpy_marks, pandas_marks):
        self.name = name
        self.age = age
        self.python_marks = python_marks
        self.numpy_marks = numpy_marks
        self.pandas_marks = pandas_marks

    def total(self):
        return self.python_marks + self.numpy_marks + self.pandas_marks

    def average(self):
        return self.total() / 3

    def result(self):
        if self.average() >= 50:
            return "Pass"
        else:
            return "Fail"


def add_student():

    # Student name validation
    while True:
        name = input("Enter student name: ")

        if name.strip() == "":
            print("Name cannot be empty")

        elif not name.isalpha():
            print("Name must contain letters only")

        else:
            break

    # Age validation
    while True:
        try:
            age = int(input("Enter student age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than 0")

        except ValueError:
            print("Please enter a valid number")

    # Python marks validation
    while True:
        try:
            python_marks = int(input("Enter Python marks: "))

            if 0 <= python_marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100")

        except ValueError:
            print("Please enter a valid number")

    # NumPy marks validation
    while True:
        try:
            numpy_marks = int(input("Enter NumPy marks: "))

            if 0 <= numpy_marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100")

        except ValueError:
            print("Please enter a valid number")

    # Pandas marks validation
    while True:
        try:
            pandas_marks = int(input("Enter Pandas marks: "))

            if 0 <= pandas_marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100")

        except ValueError:
            print("Please enter a valid number")

    # Student object
    student = Student(
        name,
        age,
        python_marks,
        numpy_marks,
        pandas_marks
    )

    return student


def view_students(students):

    for student in students:
        print("Name:", student.name)
        print("Age:", student.age)
        print("Total:", student.total())
        print("Average:", round(student.average(), 2))
        print("Result:", student.result())
        print("--------------------")


def main():

    students = []

    while True:
        print("\n======Student Management System ======")
        print("1. Add student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            student = add_student()
            students.append(student)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Program exited...")
            break

        else:
            print("please enter a valid choice ")
        

main()