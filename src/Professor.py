from src.Person import Person


class Professor(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)

    def put_grade(self, subject, semester, grade, student):
        student.grades.append({"subject":subject, "semester": semester, "value": grade, "valid": False})