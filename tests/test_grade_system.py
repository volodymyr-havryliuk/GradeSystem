import unittest

from src.DeanOfficeEmployee import DeanOfficeEmployee
from src.Professor import Professor
from src.Student import Student


class GradesSystemTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Max", "Toronii")
        self.professor = Professor("John", "Smith")
        self.dean_office_employee = DeanOfficeEmployee("Mike", "Esperanto")

    def test_student_doesnt_have_grade(self):
        self.assertIsNone(self.student.grade, "Student shouldn't have a grade initially")

    def test_students_grade_is_not_validate(self):
        self.assertFalse(self.student.is_grade_validated())

    def test_grade_has_value_after_professor_put_grade(self):
        self.professor.put_grade(5, self.student)
        self.assertIsNotNone(self.student.grade)
        self.assertFalse(self.student.is_grade_validated())

    def test_grade_is_validated_after_validation(self):
        self.dean_office_employee.validate_grade(self.student)
        self.assertTrue(self.student.is_grade_validated())


def testing_grading_functionality():
    suite = unittest.TestSuite()
    suite.addTest(GradesSystemTest('test_student_doesnt_have_grade'))
    suite.addTest(GradesSystemTest('test_students_grade_is_not_validate'))
    suite.addTest(GradesSystemTest('test_professor_put_grade'))
    return suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(testing_grading_functionality())
    unittest.main()