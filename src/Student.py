from src.Person import Person


class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)
        self._grades = []

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        self._grades = grades

    def is_grade_validated(self, index):
        return self._grades[index]['valid']

    def validate_grade(self, index):
        self._grades[index]['valid'] = True
