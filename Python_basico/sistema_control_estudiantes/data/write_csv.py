import csv


def write_csv(students):

    if not students:
        print()
        print("There are no students to export.")
        print()
        return

    with open('students.csv', 'w', newline='', encoding='utf-8') as file:

        headers = students[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        for student in students:
            writer.writerow(student)