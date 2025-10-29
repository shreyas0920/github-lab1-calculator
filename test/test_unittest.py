# import sys
# import os
# import unittest

# # Get the path to the project's root directory
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(project_root)

# from src import calculator


# class TestCalculator(unittest.TestCase):

#     def test_fun1(self):
#         self.assertEqual(calculator.fun1(2, 3), 5)
#         self.assertEqual(calculator.fun1(5, 0), 5)
#         with self.assertRaises(ValueError):
#             calculator.fun1(-1, 1)
#         with self.assertRaises(ValueError):
#             calculator.fun1(1, -1)

#     def test_fun2(self):
#         self.assertEqual(calculator.fun2(2, 3), -1)
#         self.assertEqual(calculator.fun2(5, 0), 5)
#         with self.assertRaises(ValueError):
#             calculator.fun2(-1, 1)
#         with self.assertRaises(ValueError):
#             calculator.fun2(1, -1)

#     def test_fun3(self):
#         self.assertEqual(calculator.fun3(2, 3), 6)
#         self.assertEqual(calculator.fun3(5, 0), 0)
#         with self.assertRaises(ValueError):
#             calculator.fun3(-1, 1)
#         with self.assertRaises(ValueError):
#             calculator.fun3(1, -1)

#     def test_fun4(self):
#         self.assertEqual(calculator.fun4(2, 3, 5), 10)
#         with self.assertRaises(ValueError):
#             calculator.fun4(5, 0, 1)
#         with self.assertRaises(ValueError):
#             calculator.fun4(-1, 1, 2)
#         with self.assertRaises(ValueError):
#             calculator.fun4(1, -1, 2)

#     def test_fun5(self):
#         self.assertEqual(calculator.fun5(10, 2), 5.0)
#         self.assertEqual(calculator.fun5(5, 1), 5.0)
#         with self.assertRaises(ValueError):
#             calculator.fun5(-1, 1)
#         with self.assertRaises(ValueError):
#             calculator.fun5(1, -1)
#         with self.assertRaises(ValueError):
#             calculator.fun5(10, 0)

# if __name__ == '__main__':
#     unittest.main()

import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 1), 6)  # Changed 0 to 1
        with self.assertRaises(ValueError):
            calculator.fun1(-1, 1)
        with self.assertRaises(ValueError):
            calculator.fun1(1, -1)
        with self.assertRaises(ValueError):
            calculator.fun1(5, 0)  # Test zero input

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 1), 4)  # Changed 0 to 1
        with self.assertRaises(ValueError):
            calculator.fun2(-1, 1)
        with self.assertRaises(ValueError):
            calculator.fun2(1, -1)
        with self.assertRaises(ValueError):
            calculator.fun2(5, 0)  # Test zero input

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 1), 5)  # Changed 0 to 1
        with self.assertRaises(ValueError):
            calculator.fun3(-1, 1)
        with self.assertRaises(ValueError):
            calculator.fun3(1, -1)
        with self.assertRaises(ValueError):
            calculator.fun3(5, 0)  # Test zero input

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 1, 2), 8)  # Changed 0, 1 to 1, 2
        with self.assertRaises(ValueError):
            calculator.fun4(-1, 1, 2)
        with self.assertRaises(ValueError):
            calculator.fun4(1, -1, 2)
        with self.assertRaises(ValueError):
            calculator.fun4(5, 0, 1)  # Test zero input

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5.0)
        self.assertEqual(calculator.fun5(5, 1), 5.0)
        with self.assertRaises(ValueError):
            calculator.fun5(-1, 1)
        with self.assertRaises(ValueError):
            calculator.fun5(1, -1)
        with self.assertRaises(ValueError):
            calculator.fun5(10, 0)

if __name__ == '__main__':
    unittest.main()