

def failed_students(students):
    
    failed = []

    for student in students:
        if float(student['spanish']) < 60:
            failed.append(student)
            continue

        if float(student['english']) < 60:
            failed.append(student)
            continue

        if float(student['social_studies']) < 60:
            failed.append(student)
            continue

        if float(student['science']) < 60:
            failed.append(student)
            continue
                    
    return failed