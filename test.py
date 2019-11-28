import unittest

class TestStringMethods(unittest.TestCase):

    def test_nograde(self):
        grade = ["", False]
        self.assertEqual(grade, ["", False])

    def test_notvalidatedgrade(self):
        grade = [4, False]
        self.assertEqual(grade, [4, False])

    def test_validatedgrade(self):
        grade = [4, True]
        self.assertEqual(grade, [4, True])

if __name__ == '__main__':
    unittest.main()