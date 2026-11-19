students = []

print("===== STUDENT MANAGEMENT SYSTEM =====")
print("Welcome to the system!")

while True:

    print("\n===== MAIN MENU =====")
    print("1. Register Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # REGISTER STUDENT
    if choice == "1":
        name = input("Enter student name: ").strip()
        students.append(name)
        print("Student registered successfully!")

    # VIEW STUDENTS
    elif choice == "2":
        print("\n===== REGISTERED STUDENTS =====")

        for student in students:
            print(student)

        print("Total students:", len(students))

    # SEARCH STUDENT
    elif choice == "3":
        search_name = input("Enter name to search: ").strip()

        if search_name in students:
            print("Student found!")
        else:
            print("Student not found!")

    # REMOVE STUDENT
    elif choice == "4":
        remove_name = input("Enter name to remove: ").strip()

        if remove_name in students:
            students.remove(remove_name)
            print("Student removed successfully!")
        else:
            print("Student not found!")

    # UPDATE STUDENT
    elif choice == "5":
        old_name = input("Enter name to update: ").strip()

        if old_name in students:
            new_name = input("Enter new name: ").strip()

            index = students.index(old_name)
            students[index] = new_name

            print("Student updated successfully!")
        else:
            print("Student not found!")

    # EXIT SYSTEM
    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
