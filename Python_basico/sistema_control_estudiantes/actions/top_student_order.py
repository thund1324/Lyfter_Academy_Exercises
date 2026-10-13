import csv

def order_top_students(students):
    student_list = list(students)

    for student in student_list:
        student['average'] = float(student['average'])

    student_list.sort(key=lambda x: x['average'], reverse=True)

    return student_list[:3]
