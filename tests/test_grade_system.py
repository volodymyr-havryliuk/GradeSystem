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
        self.assertEqual(len(self.student.grades), 0, "Student should NOT have a grade initially")

    def test_students_grade_is_not_validate(self, grade=3):
        self.professor.put_grade(grade, self.student)
        self.assertFalse(self.student.grades[len(self.student.grades)-1]['valid'], "Student should NOT have a validated grade")

    def test_grade_has_value_after_professor_put_grade(self, grade=5):
        self.professor.put_grade(grade, self.student)
        self.assertEqual(len(self.student.grades), 1, "Student should have one grade")
        self.assertEqual(self.student.grades[len(self.student.grades)-1]['value'], grade, "Student should have the grade with value " + str(grade))
        self.assertFalse(self.student.is_grade_validated(index=0), "Student grade should NOT have validated grade")

    def test_grade_is_validated_after_validation(self, grade=5):
        self.professor.put_grade(grade, self.student)
        self.dean_office_employee.validate_grade(self.student, index=len(self.student.grades)-1)
        self.assertEqual(len(self.student.grades), 1, "Student should have one grade")
        self.assertEqual(self.student.grades[len(self.student.grades)-1]['value'], grade, "Student should have the grade with value " + str(grade))
        self.assertTrue(self.student.is_grade_validated(index=len(self.student.grades)-1), "Student should have validated grade")

    def test_student_has_multiple_grades(self, number_grades=3, grade=4):
        for i in range(number_grades):
            self.professor.put_grade(grade, self.student)
        self.assertEqual(len(self.student.grades), number_grades, "Student should have "+ str(number_grades)+ " grades")
        for i in range(number_grades):
            self.assertFalse(self.student.is_grade_validated(index=i), "Student grade should NOT have validated grade")

    def test_dean_office_validate_one_of_many_grades(self, number_grades=3, grade=4, index_valid_grade=1):
        self.assertTrue(index_valid_grade>=0 and index_valid_grade < number_grades, "Wrong test parameters")

        for i in range(number_grades):
            self.professor.put_grade(grade, self.student)
        self.assertEqual(len(self.student.grades), number_grades, "Student should have "+ str(number_grades)+ " grades")
        self.dean_office_employee.validate_grade(self.student, index=index_valid_grade)
        for i in range(number_grades):
            if(i == index_valid_grade):
                self.assertTrue(self.student.is_grade_validated(index=index_valid_grade), "Student should have validated grade")
            else:
                self.assertFalse(self.student.is_grade_validated(index=i), "Student grade should NOT have validated grade")

    def test_dean_office_validate_all_grades(self, number_grades=3, grade=4):
        for i in range(number_grades):
            self.professor.put_grade(grade, self.student)
        for i in range(number_grades):
            self.dean_office_employee.validate_grade(self.student, index=i)
        for i in range(number_grades):
            self.assertTrue(self.student.is_grade_validated(index=i), "Student should have validated grade")

    def test_dean_office_fail_validate_grade(self, grade=1):
        self.assertTrue(grade > 5 or grade < 2, "Wrong test parameters")

        self.professor.put_grade(grade, self.student)
        self.dean_office_employee.validate_grade(self.student, index=len(self.student.grades)-1)
        self.assertFalse(self.student.is_grade_validated(index=len(self.student.grades)-1), "Student grade should NOT have validated grade")

def testing_grading_functionality():
    suite = unittest.TestSuite()
    return suite

if __name__ == '__main__':
    unittest.main()
