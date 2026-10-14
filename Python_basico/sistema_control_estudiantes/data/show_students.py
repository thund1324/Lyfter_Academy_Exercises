import csv


def shows_students(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        students = csv.DictReader(file)
        
        for student in students:
            print("-" * 5, "STUDENT INFORMATION", "-" * 5)
            for key, value in student.items():
                print(f"{key}: {value}")