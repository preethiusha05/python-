students = (
    ("Preethi",95),
    ("Anu", 85),
    ("Ravi", 42),
    ("Kiran", 76),
    ("Meena", 33),
    ("John", 90),
    ("Sara", 58)
)
student_list = list(students)
passed_students = []
failed_students = []
for name, marks in student_list:
    if marks < 35:
        failed_students.append((name, marks))
        continue   # Skip grading for failed students
    elif marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"
    passed_students.append((name, marks, grade))
distinction = [(name, marks) for name, marks in student_list if marks >= 75]
print("\n Passed Students")
for student in passed_students:
    print(student)
print("\n Failed Students")
for student in failed_students:
    print(student)
print("\n Distinction Students (>=75)")
print(distinction)
