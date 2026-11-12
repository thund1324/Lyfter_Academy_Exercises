from actions.add_student import add_student
from actions.search_student import search_student
from actions.show_students import show_students
from actions.show_failed_student import show_failed_students
from actions.top_students import show_top_students

from data.read_csv import read_csv
from data.write_csv import write_csv

def option_menu():
    print()
    students = read_csv('students.csv')
    write_csv(students)    
    
    while True:
        print("-" * 5, "STUDENT TRACKING SYSTEM", "-" * 5)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show top 3 students with the highest grade point averages")
        print("5. Show students who failed")
        print("6. Exit")
        option = input("Enter your choice (1-6): ")

        if option == '1':
            student = add_student(students)

            if student:
                students.append(student)
                write_csv(students)
        elif option == '2':
            show_students(students)
        elif option == '3':
            student_name = input("Enter the student's name to search: ")
            search_student(students, student_name)
        elif option == '4':
            show_top_students(students)
        elif option == '5':
            show_failed_students(students)
        elif option == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    print()