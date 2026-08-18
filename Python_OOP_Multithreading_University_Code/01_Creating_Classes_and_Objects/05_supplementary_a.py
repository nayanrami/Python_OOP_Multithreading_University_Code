"""Supplement: objects in a simple classroom model."""

class Classroom:
    def __init__(self, room_no):
        self.room_no = room_no
        self.students = []

    def enroll(self, name):
        self.students.append(name)

    def strength(self):
        return len(self.students)

if __name__ == "__main__":
    room = Classroom("IT-301")
    for name in ["Aman", "Het", "Mira"]:
        room.enroll(name)
    print(room.room_no, room.students, room.strength())
