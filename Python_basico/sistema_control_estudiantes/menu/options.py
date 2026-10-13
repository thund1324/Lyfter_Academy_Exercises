from actions.add_student import add_student
from actions.list_failed_students import failed_students
from actions.top_student_order import order_top_students

from data.search_student import search_student
from data.write_csv import write_csv
from data.show_students import shows_students
from data.show_failed_student import show_failed_students
from data.top_students import show_top_students


def option_menu():
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
            student = add_student(None)
            write_csv(student)
        elif option == '2':
            shows_students('students.csv')
        elif option == '3':
            student_name = input("Enter the student's name to search: ")
            search_student('students.csv', student_name)
        elif option == '4':
            show_top_students('students.csv')
        elif option == '5':
            show_failed_students('students.csv')
        elif option == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
