def create_student_grades():
    student_grades = {}
    while True:
        student_name = input("Enter student name (or 'quit' to stop): ")
        if student_name.lower() == 'quit':
            break
        grade = int(input(f"Enter grade for {student_name}: "))
        student_grades[student_name] = grade
    return student_grades
grades_dict = create_student_grades()
print("Student Grades:", grades_dict)
