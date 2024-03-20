# COMP3005
# Riyan Ahmed

import psycopg2
from psycopg2 import OperationalError
# Database connection parameters, change these as needed. 
# For the demo, we will use the following.
DB_NAME = "A3"
DB_USER = "user2"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"


def connect_db():
    """
    Connects to the database and returns a tuple of the connection and cursor, 
    otherwise it returns an Exception.
    """

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        return conn, conn.cursor()
    except OperationalError as e:
        print("Unable to connect to the database: {e}")
        return None, None


def getAllStudents(cur):
    """
    Retrieves all student records from the students table and prints them
    """
    cur.execute("SELECT * FROM students;")
    records = cur.fetchall()
    for record in records:
        print(record)

def addStudent(cur, first_name, last_name, email, enrollment_date):
    """
    Inserts a new student record into the students table
    """
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date))

def updateStudentEmail(cur, student_id, new_email):
    """
    Updates the email address for a student with the specified student_id
    """
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id))

def deleteStudent(cur, student_id):
    """
    Deletes the record of the student with the specified student_id from the students table
    """
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))


if __name__ == "__main__":
    conn, cur = connect_db() 
    if conn is None or cur is None:
        print("database could not be connected to")
    else:
        # CRUD operation calls

        # display before the crud operations
        #getAllStudents(cur)


        #addStudent(cur, 'riyan2', 'student', 'riyan2@example.com', '2000-01-01')

        #conn.commit()  # ccommit to save after db modifications

        # updateStudentEmail(cur, 4, 'carleton3@example.com')

        # conn.commit()

        deleteStudent(cur, 2)

        conn.commit()

        # display after the crud operations
        getAllStudents(cur)


        cur.close() 
        conn.close()  # close connection to the database
    