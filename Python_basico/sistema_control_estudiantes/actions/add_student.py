

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

        break

    while True:
        section = input("Enter the student's section: ")

        if not section.strip():
            print("Section cannot be empty. Please enter a valid section.")
            continue

        break

    exists = False

    for student in students:
        if student['name'].lower() == name.lower() and student['section'].lower() == section.lower():
            exists = True
            break
    
    if exists:
        print()
        print("-" * 30)
        print("-" * 5, "STUDENT ALREADY EXISTS", "-" * 5)
        print("This student already exists in this section.")
        print("Please enter a different name or section.")
        print("-" * 30)
        print()
        return None

    while True:
        try:
            spanish = float(input("Enter the student's Spanish note: "))
            if spanish >= 0 and spanish <= 100:
                break
            else:
                print("Invalid note. Please enter a note between 0 and 100.")
        except ValueError:
            print("Note must be a number.")


    while True:
        try:
            english = float(input("Enter the student's English note: "))
            if english >= 0 and english <= 100:
                break
            else:
                print("Invalid note. Please enter a note between 0 and 100.")
        except ValueError:
            print("Note must be a number.")

    while True:
        try:
            social_studies = float(input("Enter the student's Social Studies note: "))
            if social_studies >= 0 and social_studies <= 100:
                break
            else:
                print("Invalid note. Please enter a note between 0 and 100.")
        except ValueError:
            print("Note must be a number.")

    while True:
        try:
            science = float(input("Enter the student's Science note: "))
            if science >= 0 and science <= 100:
                break
            else:
                print("Invalid note. Please enter a note between 0 and 100.")
        except ValueError:
            print("Note must be a number.")

    return {
        'name': name,
        'section': section,
        'spanish': spanish,
        'english': english,
        'social_studies': social_studies,
        'science': science,
        'average': (spanish + english + social_studies + science) / 4
    }