from src.Person import Person


class DeanOfficeEmployee(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)

    def validate_grade(self, student, index):
        if(student.grades[index]['value'] >= 2 and student.grades[index]['value'] <= 5):  
            student.validate_grade(index)
