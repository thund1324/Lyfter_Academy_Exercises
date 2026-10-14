import csv

def add_student(students):
    print("-" * 5, "ADD STUDENT", "-" * 5)

    while True:
        name = input("Enter the student's name: ")

        if not name.strip():
            print("Name cannot be empty. Please enter a valid name.")
            continue
        
        if name.isnumeric():
            print("Name cannot be numeric. Please enter a valid name.")
            continue

        exists = False
        try:
            with open('students.csv', 'r', encoding='utf-8') as file:
                students = csv.DictReader(file)
                for student in students:
                    if student['name'].lower() == name.lower():
                        exists = True
                        break
        except FileNotFoundError:
            pass

        if exists:
            print("This student already exists. Please enter a different name.")
            continue
        break

    while True:
        section = input("Enter the student's section: ")
        if section.strip():
            break
        elif section.lower() == students.lower():
            print("This section already exists. Please enter a different section.")
        else:
            print("Section cannot be empty. Please enter a valid section.")

    while True:
        spanish = float(input("Enter the student's Spanish note: "))
        if spanish < 0 or spanish > 100:
            print("Invalid note. Please enter a note between 0 and 100.")
        else:
            break

    while True:
        english = float(input("Enter the student's English note: "))
        if english < 0 or english > 100:
            print("Invalid note. Please enter a note between 0 and 100.")
        else:
            break

    while True:
        social_studies = float(input("Enter the student's Social Studies note: "))
        if social_studies < 0 or social_studies > 100:
            print("Invalid note. Please enter a note between 0 and 100.")
        else:
            break

    while True:
        science = float(input("Enter the student's Science note: "))
        if science < 0 or science > 100:
            print("Invalid note. Please enter a note between 0 and 100.")
        else:
            break

    return {
        'name': name,
        'section': section,
        'spanish': spanish,
        'english': english,
        'social_studies': social_studies,
        'science': science,
        'average': (spanish + english + social_studies + science) / 4
    }

