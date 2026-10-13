import csv

def search_student(path, student_name):
    with open(path, 'r', encoding = 'utf-8') as file:
        students = csv.DictReader(file)
        found = False

        for student in students:
            if student['name'].lower() == student_name.lower():
                print("-" * 5, "STUDENT INFORMATION", "-" * 5)
                for key, value in student.items():
                    print(f"{key}: {value}")
                found = True
                break
            if not found:
                print("*" * 5, f"No student found with the name '{student_name}'.", "*" * 5)