
student = {
    'id': 6785,
    'name': 'Jhon Doe',
    'Major': 'Computing',
    'grades': {'python': 65, 'math': 47, 'os': 48},
    'phone': '6785343456'
}

#print(student['grades']['math'])

info = input("Search info for students: ")
if info in student:
    if info == 'grades':
        course = input('Which Course: ')
        print(f'Has {student[info][course]}/100 in {course}')
    else:
        print(student[info])
else:
    print(f"Info you are searching for not available or not found")