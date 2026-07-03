import json

class Student:
    def __init__(self,name,age,course):
        self. name = name
        self.age = age
        self.course = course
    def display(self):
        print("\n--------------------")
        print("students details")
        print("\n---------------------")

        print(f"name:{self.name}")
        print(f"age: {self.age}")
        print(f"course:{self.course}")

        print("\n------------------------")
    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "course": self.course
        }
# student1 = Student("jessica",18,"python")
# student1.display()

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME,"r") as file:
            data = json.load(file)
            students = []
            for student in data:
                students.append(Student(student["name"],student["age"],student["course"]))
        return students
    except FileNotFoundError:
        return[]

def save_students(students):
    data = []
    for student in students:
        data.append(student.to_dict())
    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)
students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")

        students.append(Student(name, age, course))
        save_students(students)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Found!")
        else:
            print("\n===== Student List =====")
            for student in students:
                student.display()

    elif choice == "3":
        search_name = input("Enter Student Name to Search: ")
        found = False

        for student in students:
            if student.name.lower() == search_name.lower():
                print("\nStudent Found!")
                student.display()
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        update_name = input("Enter Student Name to Update: ")
        found = False

        for student in students:
            if student.name.lower() == update_name.lower():
                student.name = input("Enter New Name: ")
                student.age = int(input("Enter New Age: "))
                student.course = input("Enter New Course: ")
                save_students(students)
                print("Student Updated Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":
        delete_name = input("Enter Student Name to Delete: ")
        found = False

        for student in students:
            if student.name.lower() == delete_name.lower():
                students.remove(student)
                save_students(students)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        
    
    
