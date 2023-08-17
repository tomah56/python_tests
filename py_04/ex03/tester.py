from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
print("\n-------\n")

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print("TypeError:", e)
try:
    student = Student(name="Bob", surname="gigi", login="toto")
    print(student)
except TypeError as e:
    print("TypeError:", e)
