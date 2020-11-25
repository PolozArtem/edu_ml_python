import unittest

from src.topic1.lesson2.string_formatting import string_formatting_task1


class MyTestCase(unittest.TestCase):

    def test_string_formatting_task1(self):
        string_formatting_task1(1)
        self.assertEqual(string_formatting_task1(1), "Hello John Doe. Your current balance is $1.00")


if __name__ == '__main__':
    unittest.main()
