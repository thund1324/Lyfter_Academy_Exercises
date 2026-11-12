import csv


def read_csv(students_file):
    students = []

    try:
        with open(students_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for student in reader:
                students.append(student)

    except FileNotFoundError:
        print()
        print("No student file was found.")
        print("A new file can be created by exporting students.")
        print()

    return students