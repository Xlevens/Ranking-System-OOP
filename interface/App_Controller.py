from tabulate import tabulate
from models.Teacher import Teacher
from models.Student_List import StudentList
from file_handling.File import FileHandler


class AppController:
    def __init__(self, teacher=None, student_list=None):
        self.teacher = teacher
        self.student_list = student_list
    
    def run(self):
        Student=input("Enter anything to start:")
        if Student=="JqR6INT":
            teacher = Teacher("Dr. Humera Tariq", "CS-352")
            students = StudentList()
            
            for s in FileHandler.load_students("results.csv"):
                students.add_student(s)

            app = AppController(teacher, students)
            app.display_results()

            

        else:
            teacher = Teacher("Dr. Humera Tariq", "CS-352")
            students = StudentList()
            
            for s in FileHandler.load_students("results.csv"):
                students.add_student(s)

            app = AppController(teacher, students)
            app.position()
            while (True):
                
                num = input("\nEnter Seat No to search: ")
                default = "B24110006"
                seat = default+num

                app.search_student(seat)
                command = input("Would you like to continue?\n")
                if(command=="exit" or seat=="Exit" or seat=="EXIT"):
                    break
        
    def position(self):
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
            if s.rank==1 or s.rank==2 or s.rank==3 or s.rank==4:
                table.append([rank_display, s.seat_no, s.name, s.q1, s.q2, s.q3, s.q4, s.q5, s.total])

        print(tabulate(table, headers, tablefmt="grid", numalign="center", stralign="center"))
        


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
