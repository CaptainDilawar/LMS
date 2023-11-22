import csv

# Utility functions
def read_csv(file_name):
    # Implement reading data from a CSV file
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def write_csv(file_name, data, append=False):
    # Implement writing data to a CSV file
    mode = "a" if append else "w"
    with open(file_name, mode, newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Define the User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Define the Admin class, inheriting from User
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    # Add additional methods for admin functionalities
    def add_new_student(self, student_username, student_password, first_name, last_name):
        # Implement adding a new student
        student_data = [student_username, student_password, first_name, last_name]
        write_csv("students.csv", student_data, append=True)

    def add_new_course(self, course_number, course_title):
        # Implement adding a new course
        course_data = [course_number, course_title]
        write_csv("courses.csv", course_data, append=True)

    def add_course_enrollment(self, student_username, course_number):
        # Implement adding a course enrollment
        enrollment_data = [student_username, course_number]
        write_csv("enrollments.csv", enrollment_data, append=True)

    def view_all_students(self):
        # Implement viewing all student information in a nicely formatted way
        students = read_csv("students.csv")
        for student in students:
            print(f"Username: {student[0]}, First Name: {student[2]}, Last Name: {student[3]}")

    def view_all_courses(self):
        # Implement viewing all course information in a nicely formatted way
        courses = read_csv("courses.csv")
        for course in courses:
            print(f"Course Number: {course[0]}, Course Title: {course[1]}")

    def view_all_enrollments(self):
        # Implement viewing all enrollment information in a nicely formatted way
        enrollments = read_csv("enrollments.csv")
        for enrollment in enrollments:
            print(f"Student Username: {enrollment[0]}, Course Number: {enrollment[1]}")

# Define the Student class, inheriting from User
class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    # Add additional methods for student functionalities
    def view_enrolled_courses(self):
        # Implement viewing all courses a student is enrolled in
        student_enrollments = read_csv("enrollments.csv")
        student_courses = [enrollment[1] for enrollment in student_enrollments if enrollment[0] == self.username]
        courses = read_csv("courses.csv")
        enrolled_courses = [course for course in courses if course[0] in student_courses]

        for course in enrolled_courses:
            print(f"Course Number: {course[0]}, Course Title: {course[1]}")

# Utility functions (in a separate file named utils.py, for example)
def read_csv(file_name):
    # Implement reading data from a CSV file
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def write_csv(file_name, data, append=False):
    # Implement writing data to a CSV file
    mode = "a" if append else "w"
    with open(file_name, mode, newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def user_verification(username, password, user_type):
    # Implement user verification based on the user type (admin or student)
    if user_type == "admin":
        admins = read_csv("admin_credentials.csv")
        return any(user[0] == username and user[1] == password for user in admins)
    elif user_type == "student":
        students = read_csv("students.csv")
        return any(user[0] == username and user[1] == password for user in students)
    else:
        return False

# Admin Module
def admin_login():
    # Implement admin login control
    attempts = 0
    while attempts < 5:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if user_verification(username, password, "admin"):
            return Admin(username, password)
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1
    print("Too many failed attempts. Exiting.")
    return None

# Student Module
def student_login():
    # Implement student login control
    attempts = 0
    while attempts < 5:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if user_verification(username, password, "student"):
            return Student(username, password)
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1
    print("Too many failed attempts. Exiting.")
    return None

# Main program
if __name__ == "__main__":
    # Your main program logic here, including calling functions based on user input
    print("Welcome!")
    user_type = input("Are you an admin or a student? ").lower()

    if user_type == "admin":
        admin = admin_login()
        if admin:
            while True:
                print("\nAdmin Menu:")
                print("1. Add a new student")
                print("2. Add a new course")
                print("3. Add a course enrollment")
                print("4. View all students")
                print("5. View all courses")
                print("6. View all enrollments")
                print("7. Logout")

                choice = input("Enter your choice: ")

                if choice == "1":
                    student_username = input("Enter student username: ")
                    student_password = input("Enter student password: ")
                    first_name = input("Enter student first name: ")
                    last_name = input("Enter student last name: ")
                    admin.add_new_student(student_username, student_password, first_name, last_name)

                elif choice == "2":
                    course_number = input("Enter course number: ")
                    course_title = input("Enter course title: ")
                    admin.add_new_course(course_number, course_title)

                elif choice == "3":
                    student_username = input("Enter student username: ")
                    course_number = input("Enter course number: ")
                    admin.add_course_enrollment(student_username, course_number)

                elif choice == "4":
                    admin.view_all_students()

                elif choice == "5":
                    admin.view_all_courses()

                elif choice == "6":
                    admin.view_all_enrollments()

                elif choice == "7":
                    print("Logging out. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

    elif user_type == "student":
        student = student_login()
        if student:
            while True:
                print("\nStudent Menu:")
                print("1. View enrolled courses")
                print("2. Logout")

                choice = input("Enter your choice: ")

                if choice == "1":
                    student.view_enrolled_courses()

                elif choice == "2":
                    print("Logging out. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

    else:
        print("Invalid user type. Exiting.")