import csv
from actions.list_failed_students import failed_students

def show_failed_students(path):
    failed = failed_students(path)

    if not failed:
        print()
        print("-" * 15)
        print("-" * 5, "NO STUDENTS HAVE FAILED", "-" * 5)
        print("-" * 15)
        return
    i = 0
    for student in failed:
        i += 1
        print("-" * 5, f"FAILED STUDENT {i + 1} INFORMATION", "-" * 5)
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish Note: {student['spanish']}")
        print(f"English Note: {student['english']}")
        print(f"Social Studies Note: {student['social_studies']}")
        print(f"Science Note: {student['science']}")
        print(f"Average Note: {float(student['average']):.2f}")
