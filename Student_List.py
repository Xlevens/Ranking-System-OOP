from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_all_students(self):
        return self.students

    def search_by_seat(self, seat_no):
        for s in self.students:
            if s.seat_no == seat_no:
                return s
        return None
