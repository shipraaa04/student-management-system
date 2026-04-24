import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()

# login function
def login():
    if username.get() == "shipra" and password.get() == "0408":
        login_window.destroy()
        open_main()
    else:
        messagebox.showerror("Error", "Invalid Login")

# main window
def open_main():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("600x450")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="🎓 Student Management System", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack()

    tk.Label(frame, text="ID", bg="#f0f0f0").grid(row=0, column=0)
    tk.Label(frame, text="Name", bg="#f0f0f0").grid(row=1, column=0)
    tk.Label(frame, text="Age", bg="#f0f0f0").grid(row=2, column=0)
    tk.Label(frame, text="Course", bg="#f0f0f0").grid(row=3, column=0)

    id_entry = tk.Entry(frame)
    name_entry = tk.Entry(frame)
    age_entry = tk.Entry(frame)
    course_entry = tk.Entry(frame)

    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    age_entry.grid(row=2, column=1)
    course_entry.grid(row=3, column=1)

    # functions
    def add_student():
        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                       (name_entry.get(), age_entry.get(), course_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Student Added")
        view_students()

    def view_students():
        for row in tree.get_children():
            tree.delete(row)
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    def update_student():
        cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?",
                       (name_entry.get(), age_entry.get(), course_entry.get(), id_entry.get()))
        conn.commit()
        messagebox.showinfo("Updated", "Student Updated")
        view_students()

    def delete_student():
        cursor.execute("DELETE FROM students WHERE id=?", (id_entry.get(),))
        conn.commit()
        messagebox.showinfo("Deleted", "Student Deleted")
        view_students()

    # buttons
    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="➕ Add", width=12, bg="#4CAF50", fg="white", command=add_student).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="🔄 Update", width=12, bg="#FFC107", command=update_student).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="❌ Delete", width=12, bg="#f44336", fg="white", command=delete_student).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="📋 View", width=12, bg="#2196F3", fg="white", command=view_students).grid(row=0, column=3, padx=5)

    # table view
    tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Course"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Course", text="Course")

    tree.pack(pady=10, fill="both", expand=True)

    root.mainloop()

# login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x220")
login_window.configure(bg="#d9edf7")

tk.Label(login_window, text="🔐 Login System", font=("Arial", 14, "bold"), bg="#d9edf7").pack(pady=10)

tk.Label(login_window, text="Username", bg="#d9edf7").pack()
username = tk.Entry(login_window)
username.pack()

tk.Label(login_window, text="Password", bg="#d9edf7").pack()
password = tk.Entry(login_window, show="*")
password.pack()

tk.Button(login_window, text="Login", bg="#007BFF", fg="white", width=10, command=login).pack(pady=10)

login_window.mainloop()