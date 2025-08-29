from tabulate import tabulate
from Teacher import Teacher
from Student_List import StudentList
from File import FileHandler


class AppController:
    def __init__(self, teacher=None, student_list=None):
        self.teacher = teacher
        self.student_list = student_list
    def run(self):
        teacher = Teacher("Dr. Humera Tariq", "CS-352")
        students = StudentList()
        for s in FileHandler.load_students("results.csv"):
            students.add_student(s)

        app = AppController(teacher, students)
        app.display_results()

        seat = input("\nEnter Seat No to search: ")
        app.search_student(seat)

        

    def assign_ranks(self):
        students = sorted(self.student_list.get_all_students(), key=lambda s: s.total, reverse=True)

        current_rank = 1
        students[0].rank = current_rank
        students[0].tie = False

        for i in range(1, len(students)):
            if students[i].total == students[i - 1].total:
                students[i].rank = students[i - 1].rank
                students[i].tie = True
                students[i - 1].tie = True
            else:
                students[i].rank = students[i - 1].rank + 1
                students[i].tie = False

        self.ranked_students = students

    def display_results(self):
        print("=" * 92)
        print("OOPs Mid Term Results (Python)".center(70))
        print("=" * 92)
        print(f"Teacher: {self.teacher.name}")
        print(f"Course Code: {self.teacher.course_code}\n")
        print("Developed By: Behroz, Fatima Shahzad, Asad, Rizwan, Syeda Kaneez Fatima, Zain.")
        print("=" * 92)

        self.assign_ranks()

        headers = ["Rank", "Seat No", "Name", "Q1", "Q2", "Q3", "Q4", "Q5", "Total"]
        table = []
        for s in self.ranked_students:
            rank_display = f"{s.rank}{'*' if s.tie else ''}"
            table.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])

        print(tabulate(table, headers, tablefmt="grid", numalign="center", stralign="center"))

    def search_student(self, seat_no):
        student = self.student_list.search_by_seat(seat_no)
        if student:
            print("\nSearch Result:")
            print(f"Seat No: {student.seat_no}")
            print(f"Name: {student.name}")
            print(f"Q1: {student.q1}, Q2: {student.q2}, Q3: {student.q3}, Q4: {student.q4}, Q5: {student.q5}")
            print(f"Total: {student.total}, Rank: {student.rank}{'*' if student.tie else ''}")
        else:
            print("\nStudent not found.")
