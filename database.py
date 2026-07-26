
import os
import sqlite3

from student import StudentInfo

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.db")


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS students( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        age INTEGER NOT NULL, 
        grade TEXT NOT NULL,
        attendance REAL NOT NULL )""")
        
    conn.commit()
    conn.close()


def add_student(student):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade, attendance) VALUES (?, ?, ?, ?)",
        (student.name, student.age, student.grade, student.attendance),
    )
    conn.commit()
    conn.close()

def get_student_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, age, grade, attendance FROM students WHERE name = ?",
        (name,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return StudentInfo(row[0], row[1], row[2], row[3])


def update_student(name, age=None, grade=None, attendance=None):
    current = get_student_by_name(name)
    if current is None:
        return

    # keep the old value wherever the user left the field blank (None)
    new_age = age if age is not None else current.age
    new_grade = grade if grade is not None else current.grade
    new_attendance = attendance if attendance is not None else current.attendance

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET age = ?, grade = ?, attendance = ? WHERE name = ?",
        (new_age, new_grade, new_attendance, name)
    )
    conn.commit()
    conn.close()


def delete_student(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def get_all_students():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade, attendance FROM students")
    rows = cursor.fetchall()
    conn.close() 

    students = []
    for (name, age, grade, attendance) in rows:
        students.append(StudentInfo(name, age, grade, attendance))
    return students
