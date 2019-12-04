from src.Person import Person


class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)
        self._grade = None
        self._is_grade_validated = False

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def is_grade_validated(self):
        return self._is_grade_validated

    def validate_grade(self):
        self._is_grade_validated = True
