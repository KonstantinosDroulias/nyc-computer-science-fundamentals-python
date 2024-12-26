student_grades = {}

student_grades['Jhon'] = 45
student_grades['Ann'] = 47
student_grades['Peter'] = 67

"""for k in student_grades:
    print(k, student_grades[k])"""

name = input("Search Name: ")
if name in student_grades:
    print(f"{name} has {student_grades[name]}/100")
else:
    print('Student Not Found') 