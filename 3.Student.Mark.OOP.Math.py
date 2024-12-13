import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []  # List of (course_name, credit, mark)

    def add_course(self, course_name, credit, mark):
        # Round down the mark to 1-digit decimal using math.floor
        rounded_mark = math.floor(mark * 10) / 10
        self.courses.append((course_name, credit, rounded_mark))

    def calculate_gpa(self):
        if not self.courses:
            return 0

        # Use numpy arrays for calculations
        credits = np.array([course[1] for course in self.courses])
        marks = np.array([course[2] for course in self.courses])

        weighted_sum = np.sum(credits * marks)
        total_credits = np.sum(credits)

        return weighted_sum / total_credits if total_credits != 0 else 0


def sort_students_by_gpa(students):
    return sorted(students, key=lambda s: s.calculate_gpa(), reverse=True)


def main_ui(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    students = []

    def add_student_ui():
        stdscr.clear()
        stdscr.addstr(0, 0, "Add New Student")

        stdscr.addstr(2, 0, "Enter Student ID: ")
        student_id = stdscr.getstr(2, 20, 20).decode("utf-8")

        stdscr.addstr(3, 0, "Enter Student Name: ")
        name = stdscr.getstr(3, 20, 20).decode("utf-8")

        student = Student(student_id, name)
        students.append(student)

    def add_course_ui():
        stdscr.clear()
        if not students:
            stdscr.addstr(0, 0, "No students available. Add a student first.")
            stdscr.getch()
            return

        stdscr.addstr(0, 0, "Add Course to Student")

        stdscr.addstr(2, 0, "Enter Student ID: ")
        student_id = stdscr.getstr(2, 20, 20).decode("utf-8")

        student = next((s for s in students if s.student_id == student_id), None)

        if not student:
            stdscr.addstr(3, 0, "Student not found.")
            stdscr.getch()
            return

        stdscr.addstr(4, 0, "Enter Course Name: ")
        course_name = stdscr.getstr(4, 20, 20).decode("utf-8")

        stdscr.addstr(5, 0, "Enter Credit: ")
        credit = int(stdscr.getstr(5, 20, 20).decode("utf-8"))

        stdscr.addstr(6, 0, "Enter Mark: ")
        mark = float(stdscr.getstr(6, 20, 20).decode("utf-8"))

        student.add_course(course_name, credit, mark)

    def display_students_ui():
        stdscr.clear()
        sorted_students = sort_students_by_gpa(students)

        stdscr.addstr(0, 0, "Student List Sorted by GPA (Descending):")
        for idx, student in enumerate(sorted_students):
            stdscr.addstr(idx + 2, 0, f"{student.student_id} - {student.name} - GPA: {student.calculate_gpa():.2f}")

        stdscr.getch()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Management System")
        stdscr.addstr(2, 0, "1. Add Student")
        stdscr.addstr(3, 0, "2. Add Course")
        stdscr.addstr(4, 0, "3. Display Students")
        stdscr.addstr(5, 0, "4. Exit")

        stdscr.addstr(7, 0, "Enter your choice: ")
        choice = stdscr.getch()

        if choice == ord('1'):
            add_student_ui()
        elif choice == ord('2'):
            add_course_ui()
        elif choice == ord('3'):
            display_students_ui()
        elif choice == ord('4'):
            break

if __name__ == "__main__":
    curses.wrapper(main_ui)
