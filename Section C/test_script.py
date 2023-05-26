from say_the_number import read_number
import unittest

class TestReadNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(read_number(0), "zero")

    def test_positive_numbers(self):
        self.assertEqual(read_number(1), "one")
        self.assertEqual(read_number(10), "ten")
        self.assertEqual(read_number(11), "eleven")

    def test_negative_numbers(self):
        self.assertEqual(read_number(-1), "negative one")
        self.assertEqual(read_number(-10), "negative ten")
        self.assertEqual(read_number(-11), "negative eleven")

    def test_teens(self):
        self.assertEqual(read_number(14), "fourteen")
        self.assertEqual(read_number(15), "fifteen")
        self.assertEqual(read_number(16), "sixteen")

    def test_tens(self):
        self.assertEqual(read_number(20), "twenty")
        self.assertEqual(read_number(30), "thirty")
        self.assertEqual(read_number(40), "forty")

    def test_hundreds(self):
        self.assertEqual(read_number(110), "one hundred and ten")
        self.assertEqual(read_number(220), "two hundred and twenty")
        self.assertEqual(read_number(350), "three hundred and fifty")
    
    def test_thousands(self):
        self.assertEqual(read_number(4110), "four thousand, one hundred and ten")
        self.assertEqual(read_number(5220), "five thousand, two hundred and twenty")
        self.assertEqual(read_number(6350), "six thousand, three hundred and fifty")


if __name__ == "__main__":
    unittest.main()