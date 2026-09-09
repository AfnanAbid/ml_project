import numpy as np

class student:
    def __init__(self, name, age, python_marks, numpy_marks, pandas_marks):
        self.name=name
        self.age=age
        self.python_marks=python_marks
        self.numpy_marks=numpy_marks
        self.pandas_marks=pandas_marks
    def total(self):
        return self.python_marks + self.numpy_marks + self.pandas_marks
    def average(self):
        return self.total() / 3
    def result(self):
         if self.average() >=50:
            return "Pass"
         else:
             return "Fail"

s1=student("Ali",24,65,95,43)
s2 = student("Ahmed", 23, 80, 70, 90)

print(s1.name)
print(s1.age)
print(s1.total())
print(round(s1.average(),2))
print(s1.result())

with open(r"C:\Users\Office\ml_project\students.txt", "w") as file:
    file.write(f"{s1.name},{s1.age},{s1.python_marks},{s1.numpy_marks},{s1.pandas_marks}")
with open(r"C:\Users\Office\ml_project\students.txt", "a") as file:
    file.write("\n")
    file.write(f"{s2.name},{s2.age},{s2.python_marks},{s2.numpy_marks},{s2.pandas_marks}")

with open(r"C:\Users\Office\ml_project\students.txt", "r") as file:
    for line in file:
        line = line.strip()
        data = line.split(",")

        name = data[0]
        age = int(data[1])
        python_marks = int(data[2])
        numpy_marks = int(data[3])
        pandas_marks = int(data[4])

        s = student(name, age, python_marks, numpy_marks, pandas_marks)

        print(s.name)
        print(s.total())
        print(round(s.average(), 2))
        print(s.result())
        print("---")

while True:
    try:
        marks = int(input("Enter marks: "))

        if 0 <= marks <= 100:
            print("Valid marks")
            break
        else:
            print("Marks must be between 0 and 100")

    except ValueError:
        print("Please enter a number")



marks = np.array([
    [65, 95, 43],
    [80, 70, 90]
])


print(marks)
print(np.shape(marks))
print(np.min(marks))
print(np.max(marks))
print(np.mean(marks))
print(np.std(marks))
print(np.sum(marks, axis=0))
print(np.sum(marks, axis=1))
print(marks[0, 0])
print(marks[0, 1])
print(marks[1, 2])
