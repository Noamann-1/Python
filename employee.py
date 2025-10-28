employees={}
def addEmployee():
    id = input("Enter Employee ID: ")
    if id in employees:
        print(" Employee already exists!")
        return
    name = input("Enter Name: ")
    ph = input("Enter Phone Number: ")
    salary = input("Enter Salary: ")
    desig=input("Enter Designation: ")

    employees[id] = {"name": name, "ph": ph, "salary": salary , "desig":desig}
    print(" Employee added successfully!")
def deleteEmployee():
    id = input("Enter Employee ID: ")
    if id in employees:
        del employees[id]
        print(" Employee deleted successfully!")
    else:
        print(" Employee not found!")

def updateEmployee():
    id = input("Enter Employee ID: ")
    if id in employees:
        print("Current details:", employees[id])
        name = input("Enter Name: ")
        ph = input("Enter Phone Number: ")
        salary = input("Enter Salary: ")
        desig=input("Enter Designation: ")

        if name:
            students[roll]["name"] = name
        if age:
            students[roll]["age"] = age
        if marks:
            students[roll]["marks"] = marks
        
        print("Student updated successfully!")
    else:
        print(" Student not found!")

def display_students():
    if not students:
        print("No students found!")
        return
    print("\nStudent Records:")
    for roll, info in students.items():
        print(f"Roll No: {roll}, Name: {info['name']}, Age: {info['age']}, Marks: {info['marks']}")
def count_students():
    i=0
    for roll in students:
        i+=1
    print(f"Number of students = {i}")
        

while True:
        print("\n--------Student Management System---------")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Number Of Students")
        print("6. Exit The Program")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            count_students()
        else:
            print("EXiting.....")
            break
    
