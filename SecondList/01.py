def add_student():
    student_name = input("\nEnter the name of the student to be added: ")
    students.append(student_name)
    print(f"\nThe student {student_name} has been added to the list.\n")

def search_student():
    student_name = input("\nEnter the name of the student to search for: ")
    if student_name in students: 
        print(f"\nThe student {student_name} is in the list.\n")
    else:
        print(f"\nThe student {student_name} is not in the list.\n")

def display_in_alphabetical_order():
    sorted_students = sorted(students)
    print("\nList of students in alphabetical order:\n")
    for student in sorted_students:
        print("-",student)

def remove_student():
    student_name = input("\nEnter the name of the student to be removed: ")
    if student_name in students:
        students.remove(student_name)
        print(f"\nThe student {student_name} has been removed from the list.\n")
    else:
        print(f"\nThe student {student_name} is not in the list.\n")


    
if __name__ == "__main__":
    students = []
    option = 0
    while option != 5:
        print("\nOptions:")
        print("1 - Add student")
        print("2 - Search student")
        print("3 - Display list of students in alphabetical order")
        print("4 - Remove student")
        print("5 - Exit the program")

        option = int(input("Enter the number of the desired option: "))

        if option == 1:
            add_student()
        elif option == 2:
            search_student()
        elif option == 3:
            display_in_alphabetical_order()
        elif option == 4:
            remove_student()
        elif option == 5:
            print("Exiting the program...")
        else:
            print("\nInvalid option. Please choose a valid option.")
