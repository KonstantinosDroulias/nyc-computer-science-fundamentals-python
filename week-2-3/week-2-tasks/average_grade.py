grade = int(input("Grade: "))
grade_list = []

while True:
    grade_list.append(grade)
    user_input = input("Continue 'yes/no': ")
    user_input = user_input.strip()
    

    if user_input == 'yes':
        grade = int(input("Grade: "))
    elif user_input == 'no':
        avg_grade = sum(grade_list) / len(grade_list)
        print(f"AVERAGE: {avg_grade}")
        break
        