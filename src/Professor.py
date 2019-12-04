from src.Person import Person


class Professor(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)

    def put_grade(self, grade, student):
        student.grade = grade
