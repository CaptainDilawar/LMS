import csv

def create_admin_credentials():
    with open("admin_credentials.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Add dummy admin credentials
        writer.writerow(["admin1", "password1"])
        writer.writerow(["admin2", "password2"])
        writer.writerow(["admin3", "password3"])

def create_students():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Add dummy student data
        writer.writerow(["student1", "password1", "John", "Doe"])
        writer.writerow(["student2", "password2", "Jane", "Smith"])
        writer.writerow(["student3", "password3", "Bob", "Johnson"])

def create_courses():
    with open("courses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Add dummy course data
        writer.writerow(["CSCI101", "Introduction to Computer Science"])
        writer.writerow(["MATH201", "Calculus I"])
        writer.writerow(["ENG101", "English Composition"])

def create_enrollments():
    with open("enrollments.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Add dummy enrollment data
        writer.writerow(["student1", "CSCI101"])
        writer.writerow(["student1", "MATH201"])
        writer.writerow(["student2", "ENG101"])

if __name__ == "__main__":
    # Create the CSV files with dummy data
    create_admin_credentials()
    create_students()
    create_courses()
    create_enrollments()

    print("CSV files created with dummy data.")
