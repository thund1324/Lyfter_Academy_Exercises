from actions.list_failed_students import failed_students


def show_failed_students(students):
    failed = failed_students(students)

    if not failed:
        print()
        print("-" * 30)
        print("-" * 5, "NO STUDENTS HAVE FAILED",   "-" * 5)
        print("-" * 30)
        print()
        return
    i = 0
    for student in failed:
        i += 1
        print("-" * 5, f"FAILED STUDENT {i} INFORMATION", "-" * 5)
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print("Failed Subjects:")

        if float(student['spanish']) < 60:
            print(f"Spanish: {student['spanish']}")

        if float(student['english']) < 60:
            print(f"English: {student['english']}")

        if float(student['social_studies']) < 60:
            print(f"Social Studies: {student['social_studies']}")

        if float(student['science']) < 60:
            print(f"Science: {student['science']}")

        print()