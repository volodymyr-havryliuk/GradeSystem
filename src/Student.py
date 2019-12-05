from src.Person import Person


class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)
        self._grade = []
        self._grade_validation = []

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @property
    def grade_validation(self):
        return self._grade_validation

    @grade_validation.setter
    def grade_validation(self, grade_validation):
        self._grade_validation = grade_validation


    def is_grade_validated(self, index):
        return self._grade_validation[index]

    def validate_grade(self, index):
        self._grade_validation[index] = True
