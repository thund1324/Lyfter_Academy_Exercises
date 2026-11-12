

def show_students(students):
    if not students:
        print()
        print("-" * 30)
        print("-" * 5, "NO STUDENTS FOUND", "-" * 5)
        print("-" * 30)
        print()
        return

    for student in students:
        print("-" * 5, "STUDENT INFORMATION", "-" * 5)
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social Studies: {student['social_studies']}")
        print(f"Science: {student['science']}")
        print(f"Average: {student['average']}")
        print()