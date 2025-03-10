students = {
	10: {'name': 'Russell Lopez', 'grades': [45, 34, 67, 45, 0, 34]},
    11: {'name': 'Theresa Campbell', 'grades': [40, 34, 20, 44, 56, 18, 34, 35]},
    12: {'name': 'Martin Roy', 'grades': [46, 55, 71, 67, 55, 64]},
    13: {'name': 'Nicole Young', 'grades': [40, 38, 42, 42, 51]},
    14: {'name': 'Elizabeth Diaz', 'grades': [44]},
    15: {'name': 'Susan Coleman', 'grades': [56, 19, 55, 34, 30, 18]},
}

below_grade_students = {}

for student_id, student_data in students.items():
    grades = student_data['grades']
    names = student_data['name']
    for grade in grades:
        grade += grade
    avg_grade = grade / len(grades)
    if avg_grade <= 40:
        below_grade_students[names] = avg_grade
        
print(below_grade_students)
        
        