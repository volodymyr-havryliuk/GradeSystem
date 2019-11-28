import unittest

class TestStringMethods(unittest.TestCase):

    def test_nograde(self):
        grade = ["", False]
        self.assertEqual(grade, ["", False])

    def test_notvalidatedgrade(self):
        self.assertEqual([4, False], [4, False])

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()