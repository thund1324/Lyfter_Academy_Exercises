from actions.top_student_order import order_top_students


def show_top_students(students):
    
    if not students:
        print()
        print("-" * 30)
        print("-" * 5, "NO STUDENTS FOUND", "-" * 5)
        print("-" * 30)
        print()
        return

    top3 = order_top_students(students)

    i = 0

    print("-" * 5, "TOP 3 STUDENTS", "-" * 5)

    for student in top3:
        i += 1

        print("-" * 5, f"STUDENT NUMBER {i} INFORMATION", "-" * 5)
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish Note: {student['spanish']}")
        print(f"English Note: {student['english']}")
        print(f"Social Studies Note: {student['social_studies']}")
        print(f"Science Note: {student['science']}")
        print(f"Average Note: {float(student['average']):.2f}")
        print()