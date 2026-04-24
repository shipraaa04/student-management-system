import sqlite3

# database connect
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()

# functions
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    
    if data:
        for row in data:
            print(row)
    else:
        print("No records found.")

def update_student():
    id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, id))
    conn.commit()
    print("Student updated successfully!")

def delete_student():
    id = int(input("Enter student ID to delete: "))
    
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Student deleted successfully!")

# main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again!")