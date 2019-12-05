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
        self.assertEqual(len(self.student.grade), 0, "Student should NOT have a grade initially")

    def test_students_grade_is_not_validate(self):
        self.assertEqual(len(self.student.grade_validation), 0, "Student should NOT have a validated grade")

    def test_grade_has_value_after_professor_put_grade(self):
        self.professor.put_grade(5, self.student)
        self.assertEqual(len(self.student.grade), 1, "Student should have one grade")
        self.assertFalse(self.student.is_grade_validated(index=0), "Student grade should NOT have validated grade")

    def test_grade_is_validated_after_validation(self):
        self.professor.put_grade(5, self.student)
        self.assertEqual(len(self.student.grade), 1, "Student should have one grade")
        self.dean_office_employee.validate_grade(self.student, index=0)
        self.assertTrue(self.student.is_grade_validated(index=0), "Student should have validated grade")


def testing_grading_functionality():
    suite = unittest.TestSuite()
    suite.addTest(GradesSystemTest('test_student_doesnt_have_grade'))
    suite.addTest(GradesSystemTest('test_students_grade_is_not_validate'))
    suite.addTest(GradesSystemTest('test_grade_has_value_after_professor_put_grade'))
    suite.addTest(GradesSystemTest('test_grade_is_validated_after_validation'))
    return suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(testing_grading_functionality())
    unittest.main()
