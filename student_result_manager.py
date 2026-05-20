student = {}

while True:
    print("\n----STUDENT MANAGER APP----")
    print("1. Add Student")
    print("2. View Student")    
    print("3. Check Student")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        student[name] = marks
        print(f"{name} successfully added!")
    elif choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\n----STUDENT DETAILS----")
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")
    elif choice == '3':
        name = input("Enter student name to check: ")
        if name in student:
            marks = student[name]
            print(f"Marks: {marks}")
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print(f"{name} is not found in the records.")
    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")          