import unittest

from src.topic1.lesson1.variables import variables_task1


class MyTestCase(unittest.TestCase):

    def test_variables_task1(self):
        my_string, my_float, my_int = variables_task1()
        self.assertEqual(my_string, "hello World"
        self.assertEqual(my_float, 1.02)
        self.assertEqual(my_int, 1)


if __name__ == '__main__':
    unittest.main()
