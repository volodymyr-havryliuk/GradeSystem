import unittest
from student import Student

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.student = Student(["", False])

    def test_nograde(self):
        testArray=["", False]
        self.assertEqual(self.student.getGrade(), testArray)

    def test_notvalidatedgrade(self):
        grade = [4, False]
        self.assertEqual(grade, [4, False])

    def test_validatedgrade(self):
        grade = [4, True]
        self.assertEqual(grade, [4, True])

if __name__ == '__main__':
    unittest.main()