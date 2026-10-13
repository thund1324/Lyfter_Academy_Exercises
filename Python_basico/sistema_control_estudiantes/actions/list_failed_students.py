import csv

def failed_students(path):
    with open(path, 'r', encoding='utf-8') as file:
        students = csv.DictReader(file)
        failed = []

        for student in students:
            if float(student['average']) < 60:
                failed.append(student)

    return failed