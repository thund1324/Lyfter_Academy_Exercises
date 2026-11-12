

def search_student(students, student_name):

    if not students:
        print()
        print("-" * 30)
        print("-" * 5, "NO STUDENTS FOUND", "-" * 5)
        print("-" * 30)
        print()
        return

    found = False

    for student in students:
        if student['name'].lower() == student_name.lower():
            print("-" * 5, "STUDENT INFORMATION", "-" * 5)
            
            for key, value in student.items():
                print(f"{key}: {value}")
                
            found = True
            break

    if not found:
        print()
        print("-" * 30)
        print("-" * 5, "STUDENT NOT FOUND", "-" * 5)
        print("-" * 30)
        print()