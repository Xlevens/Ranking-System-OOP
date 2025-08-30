import csv, os
from models.Student import Student

class FileHandler:
    @staticmethod
    def load_students(filename="results.csv"):
        students = []
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", filename)

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 8:  # must be 8 fields
                    seat_no, name, q1, q2, q3, q4, q5, total = row
                    students.append(Student(seat_no, name, q1, q2, q3, q4, q5, total))
        return students
