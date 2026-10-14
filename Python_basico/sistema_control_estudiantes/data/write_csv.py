import csv
    
def write_csv(student):
    file_exists = False
    try:
        with open('students.csv', 'r', encoding='utf-8') as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open('students.csv', 'a', newline='', encoding='utf-8') as file:
        headers = student.keys()
        writer = csv.DictWriter(file, fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        writer.writerow(student)