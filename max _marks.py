no_of_students = int(input("Enter number of students: "))
marks = {}
for i in range(no_of_students):
    name = input("Enter name of student: ")
    mark = int(input("Enter marks of student: "))
    marks[name] = mark
max_mark = max(marks.values())
print("Top student with highest marks:")
for name, mark in marks.items():
    if mark == max_mark:
        print(f"{name}: {mark}")
