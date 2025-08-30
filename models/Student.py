class Student:
    def __init__(self, seat_no, name, q1, q2, q3, q4, q5, total):
        self.seat_no = seat_no
        self.name = name
        self.q1 = float(q1)
        self.q2 = float(q2)
        self.q3 = float(q3)
        self.q4 = float(q4)
        self.q5 = float(q5)
        self.total = float(total)
        self.rank = None
        self.tie = False
